<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api'
import { Modal } from 'bootstrap'

const endpoint = '/genre-in-games/'

const items = ref([])
const genres = ref([])
const games = ref([])
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
    const [list, genreList, gameList] = await Promise.all([
      api.get(endpoint),
      api.get('/genres/'),
      api.get('/games/'),
    ])
    items.value = list.data
    genres.value = genreList.data
    games.value = gameList.data
  } catch (e) {
    error.value = 'Не удалось загрузить список'
  }
}

function openCreate() {
  editing.value = false
  form.value = { id_genre: '', id_game: '' }
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
      id_genre: form.value.id_genre || null,
      id_game: form.value.id_game || null,
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
      <h1 class="h3 mb-0">Жанры в играх</h1>
      <button class="btn btn-primary" @click="openCreate">Создать</button>
    </div>

    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <table class="table table-striped align-middle">
      <thead>
        <tr>
          <th style="width: 60px">ID</th>
          <th>Игра</th>
          <th>Жанр</th>
          <th style="width: 200px">Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ entityName(games, item.id_game) }}</td>
          <td>{{ entityName(genres, item.id_genre) }}</td>
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
                {{ editing ? 'Изменение связи' : 'Новая связь жанра и игры' }}
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
                <label class="form-label">Жанр</label>
                <select v-model="form.id_genre" required class="form-select">
                  <option value="" disabled>Выберите жанр</option>
                  <option v-for="genre in genres" :key="genre.id" :value="genre.id">
                    {{ genre.name }}
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
