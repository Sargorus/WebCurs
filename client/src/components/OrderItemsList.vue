<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api'
import { Modal } from 'bootstrap'

const endpoint = '/order-items/'

const items = ref([])
const orders = ref([])
const halls = ref([])
const gameSets = ref([])
const error = ref('')
const editing = ref(false)
const form = ref({})

function entityName(list, id) {
  const found = list.value.find((i) => i.id === id)
  if (!found) return '—'
  return found.name ?? `Заказ ${found.id}`
}

function toLocalInput(iso) {
  if (!iso) return ''
  const d = new Date(iso)
  if (Number.isNaN(d.getTime())) return ''
  const pad = (n) => String(n).padStart(2, '0')
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}T${pad(d.getHours())}:${pad(d.getMinutes())}`
}

function toIso(local) {
  if (!local) return ''
  return local.length === 16 ? `${local}:00Z` : local
}

async function load() {
  error.value = ''
  try {
    const [list, orderList, hallList, setList] = await Promise.all([
      api.get(endpoint),
      api.get('/orders/'),
      api.get('/halls/'),
      api.get('/game-sets/'),
    ])
    items.value = list.data.map((i) => ({
      ...i,
      start_time_local: toLocalInput(i.start_time),
      end_time_local: toLocalInput(i.end_time),
    }))
    orders.value = orderList.data
    halls.value = hallList.data
    gameSets.value = setList.data
  } catch (e) {
    error.value = 'Не удалось загрузить список'
  }
}

function openCreate() {
  editing.value = false
  form.value = {
    start_time_local: '',
    end_time_local: '',
    game_set_price: 500,
    hall_price: 300,
    id_order: '',
    id_hall: '',
    id_game_set: '',
  }
  error.value = ''
  showModal.value = true
}

function openEdit(item) {
  editing.value = true
  form.value = {
    ...item,
    start_time_local: item.start_time_local ?? toLocalInput(item.start_time),
    end_time_local: item.end_time_local ?? toLocalInput(item.end_time),
    id_order: item.id_order ?? '',
    id_hall: item.id_hall ?? '',
    id_game_set: item.id_game_set ?? '',
  }
  error.value = ''
  showModal.value = true
}

async function save() {
  error.value = ''
  try {
    const payload = {
      start_time: toIso(form.value.start_time_local),
      end_time: toIso(form.value.end_time_local),
      game_set_price: Number(form.value.game_set_price),
      hall_price: Number(form.value.hall_price),
      id_order: form.value.id_order || null,
      id_hall: form.value.id_hall || null,
      id_game_set: form.value.id_game_set || null,
    }
    if (editing.value) {
      await api.put(`${endpoint}${form.value.id}/`, payload)
    } else {
      await api.post(endpoint, payload)
    }
    showModal.value = false
    await load()
  } catch (e) {
    error.value = e.response?.data ? JSON.stringify(e.response.data) : 'Ошибка сохранения'
  }
}

async function remove(item) {
  if (!confirm(`Удалить позицию #${item.id}?`)) return
  error.value = ''
  try {
    await api.delete(`${endpoint}${item.id}/`)
    await load()
  } catch (e) {
    error.value = 'Не удалось удалить запись'
  }
}

onMounted(load)
</script>

<template>
  <div class="container">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h1 class="h3 mb-0">Позиции заказов</h1>
      <button class="btn btn-primary" @click="openCreate">Создать</button>
    </div>

    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <table class="table table-striped align-middle">
      <thead>
        <tr>
          <th style="width: 60px">ID</th>
          <th>Заказ</th>
          <th>Зал</th>
          <th>Набор</th>
          <th>Начало</th>
          <th>Конец</th>
          <th>Цена набора, ₽/ч</th>
          <th>Цена зала, ₽/ч</th>
          <th style="width: 200px">Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ entityName(orders, item.id_order) }}</td>
          <td>{{ entityName(halls, item.id_hall) }}</td>
          <td>{{ entityName(gameSets, item.id_game_set) }}</td>
          <td>{{ item.start_time_local.replace('T', ' ') }}</td>
          <td>{{ item.end_time_local.replace('T', ' ') }}</td>
          <td>{{ item.game_set_price }}</td>
          <td>{{ item.hall_price }}</td>
          <td>
            <button class="btn btn-sm btn-outline-primary me-2" @click="openEdit(item)">
              Изменить
            </button>
            <button class="btn btn-sm btn-outline-danger" @click="remove(item)">Удалить</button>
          </td>
        </tr>
        <tr v-if="!items.length">
          <td colspan="9" class="text-center text-muted">Записей нет</td>
        </tr>
      </tbody>
    </table>

    <div v-if="showModal" class="modal fade show d-block" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <form @submit.prevent.stop="save">
            <div class="modal-header">
              <h5 class="modal-title">
                {{ editing ? 'Изменение позиции' : 'Новая позиция заказа' }}
              </h5>
              <button type="button" class="btn-close" @click="showModal = false"></button>
            </div>
            <div class="modal-body">
              <div class="mb-3">
                <label class="form-label">Заказ</label>
                <select v-model="form.id_order" class="form-select">
                  <option value="">— не выбран —</option>
                  <option v-for="order in orders" :key="order.id" :value="order.id">
                    Заказ {{ order.id }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Зал</label>
                <select v-model="form.id_hall" class="form-select">
                  <option value="">— не выбран —</option>
                  <option v-for="hall in halls" :key="hall.id" :value="hall.id">
                    {{ hall.name }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Игровой набор</label>
                <select v-model="form.id_game_set" class="form-select">
                  <option value="">— не выбран —</option>
                  <option v-for="set in gameSets" :key="set.id" :value="set.id">
                    {{ set.name }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Время начала</label>
                <input v-model="form.start_time_local" required type="datetime-local" class="form-control" />
              </div>
              <div class="mb-3">
                <label class="form-label">Время конца</label>
                <input v-model="form.end_time_local" required type="datetime-local" class="form-control" />
              </div>
              <div class="mb-3">
                <label class="form-label">Цена набора, ₽/ч</label>
                <input
                  v-model.number="form.game_set_price"
                  required
                  type="number"
                  min="0"
                  class="form-control"
                />
              </div>
              <div class="mb-3">
                <label class="form-label">Цена зала, ₽/ч</label>
                <input
                  v-model.number="form.hall_price"
                  required
                  type="number"
                  min="0"
                  class="form-control"
                />
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" @click="showModal = false">
                Отмена
              </button>
              <button type="submit" class="btn btn-primary">Сохранить</button>
            </div>
          </form>
        </div>
      </div>
      <div class="modal-backdrop fade show"></div>
    </div>
  </div>
</template>
