<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api'
import { Modal } from 'bootstrap'

const endpoint = '/game-on-sets/'

const items = ref([])
const games = ref([])
const gameSets = ref([])
const error = ref('')
const editing = ref(false)
const form = ref({})

function entityName(list, id) {
  const found = list.value.find((i) => i.id === id)
  return found ? found.name : '—'
}

async function load() {
  error.value = ''
  try {
    const [list, gameList, setList] = await Promise.all([
      api.get(endpoint),
      api.get('/games/'),
      api.get('/game-sets/'),
    ])
    items.value = list.data
    games.value = gameList.data
    gameSets.value = setList.data
  } catch (e) {
    error.value = 'Не удалось загрузить список'
  }
}

function openCreate() {
  editing.value = false
  form.value = { id_game: '', id_game_set: '' }
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
    const payload = {
      id_game: form.value.id_game || null,
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
  if (!confirm(`Удалить связь #${item.id}?`)) return
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
      <h1 class="h3 mb-0">Игры на игровых наборах</h1>
      <button class="btn btn-primary" @click="openCreate">Создать</button>
    </div>

    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <table class="table table-striped align-middle">
      <thead>
        <tr>
          <th style="width: 60px">ID</th>
          <th>Игра</th>
          <th>Игровой набор</th>
          <th style="width: 200px">Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ entityName(games, item.id_game) }}</td>
          <td>{{ entityName(gameSets, item.id_game_set) }}</td>
          <td>
            <button class="btn btn-sm btn-outline-primary me-2" @click="openEdit(item)">
              Изменить
            </button>
            <button class="btn btn-sm btn-outline-danger" @click="remove(item)">Удалить</button>
          </td>
        </tr>
        <tr v-if="!items.length">
          <td colspan="4" class="text-center text-muted">Записей нет</td>
        </tr>
      </tbody>
    </table>

    <div v-if="showModal" class="modal fade show d-block" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <form @submit.prevent.stop="save">
            <div class="modal-header">
              <h5 class="modal-title">
                {{ editing ? 'Изменение связи' : 'Новая связь игры и набора' }}
              </h5>
              <button type="button" class="btn-close" @click="showModal = false"></button>
            </div>
            <div class="modal-body">
              <div class="mb-3">
                <label class="form-label">Игра</label>
                <select v-model="form.id_game" required class="form-select">
                  <option value="" disabled>Выберите игру</option>
                  <option v-for="game in games" :key="game.id" :value="game.id">
                    {{ game.name }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Игровой набор</label>
                <select v-model="form.id_game_set" required class="form-select">
                  <option value="" disabled>Выберите набор</option>
                  <option v-for="set in gameSets" :key="set.id" :value="set.id">
                    {{ set.name }}
                  </option>
                </select>
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
