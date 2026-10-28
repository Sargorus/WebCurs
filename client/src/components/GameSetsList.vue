<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api'
import { Modal } from 'bootstrap'

const endpoint = '/game-sets/'

const items = ref([])
const error = ref('')
const editing = ref(false)
const form = ref({})

async function load() {
  error.value = ''
  try {
    const { data } = await api.get(endpoint)
    items.value = data
  } catch (e) {
    error.value = 'Не удалось загрузить список'
  }
}

function openCreate() {
  editing.value = false
  form.value = { name: '', description: '', price_per_hour: 500 }
  error.value = ''
  showModal.value = true
}

function openEdit(item) {
  editing.value = true
  form.value = { ...item }
  error.value = ''
  showModal.value = true
}

async function save() {
  error.value = ''
  try {
    const payload = { ...form.value, price_per_hour: Number(form.value.price_per_hour) }
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
  if (!confirm(`Удалить набор «${item.name}»?`)) return
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
      <h1 class="h3 mb-0">Игровые наборы</h1>
      <button class="btn btn-primary" @click="openCreate">Создать</button>
    </div>

    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <table class="table table-striped align-middle">
      <thead>
        <tr>
          <th style="width: 60px">ID</th>
          <th>Название</th>
          <th>Описание</th>
          <th>Цена за час, ₽</th>
          <th style="width: 200px">Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.description }}</td>
          <td>{{ item.price_per_hour }}</td>
          <td>
            <button class="btn btn-sm btn-outline-primary me-2" @click="openEdit(item)">
              Изменить
            </button>
            <button class="btn btn-sm btn-outline-danger" @click="remove(item)">Удалить</button>
          </td>
        </tr>
        <tr v-if="!items.length">
          <td colspan="5" class="text-center text-muted">Записей нет</td>
        </tr>
      </tbody>
    </table>

    <div v-if="showModal" class="modal fade show d-block" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <form @submit.prevent.stop="save">
            <div class="modal-header">
              <h5 class="modal-title">
                {{ editing ? 'Изменение набора' : 'Новый игровой набор' }}
              </h5>
              <button type="button" class="btn-close" @click="showModal = false"></button>
            </div>
            <div class="modal-body">
              <div class="mb-3">
                <label class="form-label">Название</label>
                <input v-model="form.name" required type="text" class="form-control" />
              </div>
              <div class="mb-3">
                <label class="form-label">Описание</label>
                <textarea v-model="form.description" required class="form-control" rows="3"></textarea>
              </div>
              <div class="mb-3">
                <label class="form-label">Цена в рублях за час</label>
                <input
                  v-model.number="form.price_per_hour"
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
