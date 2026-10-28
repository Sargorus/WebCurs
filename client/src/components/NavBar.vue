<script setup>
import useProfileStore from '@/stores/profileStore'
import { storeToRefs } from 'pinia'

const profileStore = useProfileStore()
const { isAuthenticated, userName } = storeToRefs(profileStore)

async function onLogoutButtonClick() {
  await profileStore.logout()
}
</script>

<template>
  <nav class="navbar navbar-expand-sm bg-body-tertiary mb-3">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">VRclub</router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse w-100 justify-content-between" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Главная</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/login">Вход</router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/admin/">Админка</a>
          </li>
        </ul>
        <div role="search">
          Авторизован: {{ userName }}
          <button
            v-if="isAuthenticated"
            class="btn btn-outline-success ms-2"
            @click="onLogoutButtonClick"
          >
            Выйти
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>
