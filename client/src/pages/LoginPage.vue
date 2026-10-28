<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { storeToRefs } from 'pinia'
import useProfileStore from '@/stores/profileStore'

const profileStore = useProfileStore()
const { isAuthenticated, error, loading } = storeToRefs(profileStore)

const router = useRouter()

const username = ref('')
const password = ref('')

async function onLoginClick() {
  const ok = await profileStore.login(username.value, password.value)
  if (ok) {
    await router.push('/')
  }
}
</script>

<template>
  <div class="d-flex justify-content-center p-4">

    <form style="width: 350px" @submit.prevent.stop="onLoginClick">
      <h1 class="h4 mb-3">Вход</h1>
      <div v-if="error" class="alert alert-danger py-2">{{ error }}</div>
      <div class="mb-3">
        <label class="form-label">Логин</label>
        <input v-model="username" required type="text" class="form-control" />
      </div>
      <div class="mb-3">
        <label class="form-label">Пароль</label>
        <input v-model="password" required type="password" class="form-control" />
      </div>
      <button class="btn btn-primary" :disabled="loading">
        {{ loading ? 'Вход...' : 'Войти' }}
      </button>
      <div v-if="isAuthenticated" class="text-success mt-2">Вы уже авторизованы</div>
    </form>
    <div class="text-center mt-3">
     Нет аккаунта?
    <router-link to="/register">Зарегистрироваться</router-link>
    </div>
  </div>
</template>
