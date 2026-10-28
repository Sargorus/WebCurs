<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import useProfileStore from '@/stores/profileStore'

const router = useRouter()
const profileStore = useProfileStore()

const username = ref('')
const password = ref('')

async function handleRegister() {
  const ok = await profileStore.register(username.value, password.value)
  if (ok) {
    router.push({ name: 'main' })
  }
}
</script>

<template>
  <div class="container d-flex justify-content-center mt-5">
    <div class="card p-4" style="max-width: 400px; width: 100%">
      <h2 class="mb-3">Регистрация</h2>

      <div v-if="profileStore.error" class="alert alert-danger">
        {{ profileStore.error }}
      </div>

      <form @submit.prevent="handleRegister">
        <div class="mb-3">
          <label for="username" class="form-label">Имя пользователя</label>
          <input type="text" id="username" v-model="username" class="form-control" required />
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Пароль</label>
          <input type="password" id="password" v-model="password" class="form-control" required />
        </div>
        <button type="submit" class="btn btn-primary w-100" :disabled="profileStore.loading">
          Зарегистрироваться
        </button>
      </form>

      <div class="text-center mt-3">
        Уже есть аккаунт?
        <router-link to="/login">Войти</router-link>
      </div>
    </div>
  </div>
</template>
