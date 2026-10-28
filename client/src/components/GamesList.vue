<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api'
import { Modal } from 'bootstrap'

const endpoint = '/games/'

const items = ref([])
const error = ref('')
const editing = ref(false)
const form = ref({})

const modalRef = ref(null)
let modalInstance = null

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
  form.value = { name: '', description: '', poster: '' }
  error.value = ''
  if (modalInstance) modalInstance.show()
}

function openEdit(item) {
  editing.value = true
  form.value = { ...item }
  error.value = ''
  if (modalInstance) modalInstance.show()
}

async function save() {
  error.value = ''
  try {
    const payload = { ...form.value }
    if (!payload.poster) delete payload.poster
    if (editing.value) {
      await api.put(`${endpoint}${form.value.id}/`, payload)
    } else {
      await api.post(endpoint, payload)
    }
    if (modalInstance) modalInstance.hide()
    await load()
  } catch (e) {
    error.value = e.response?.data ? JSON.stringify(e.response.data) : 'Ошибка сохранения'
  }
}

async function remove(item) {
  if (!confirm(`Удалить игру «${item.name}»?`)) return
  error.value = ''
  try {
    await api.delete(`${endpoint}${item.id}/`)
    await load()
  } catch (e) {
    error.value = 'Не удалось удалить запись'
  }
}

function posterUrl(item) {
  if (!item.poster) return ''
  return item.poster.startsWith('/') ? item.poster : `/${item.poster}`
}

onMounted(() => {
  if (modalRef.value) {
    modalInstance = new Modal(modalRef.value)
  }
  load()
})
</script>

<template>
  <div class="container">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h1 class="h3 mb-0">Игры</h1>
      <button class="btn btn-primary" @click="openCreate">Создать</button>
    </div>

    <div v-if="error" class="alert alert-danger">{{ error }}</div>

    <table class="table table-striped align-middle">
      <thead>
        <tr>
          <th style="width: 60px">ID</th>
          <th style="width: 90px">Постер</th>
          <th>Название</th>
          <th>Описание</th>
          <th style="width: 200px">Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.id }}</td>
          <td>
            <img
              v-if="item.poster"
              :src="posterUrl(item)"
              :alt="item.name"
              style="max-width: 70px; max-height: 70px"
              class="rounded"
            />
          </td>
          <td>{{ item.name }}</td>
          <td>{{ item.description }}</td>
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

    <div ref="modalRef" class="modal fade" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <form @submit.prevent.stop="save">
            <div class="modal-header">
              <h5 class="modal-title">{{ editing ? 'Изменение игры' : 'Новая игра' }}</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
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
                <label class="form-label">Постер (файл в media/posters)</label>
                <input
                  v-model="form.poster"
                  type="text"
                  class="form-control"
                  placeholder="posters/example.png"
                />
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                Отмена
              </button>
              <button type="submit" class="btn btn-primary">Сохранить</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
