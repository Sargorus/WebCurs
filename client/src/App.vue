<script setup>

import { onBeforeMount } from 'vue'
import NavBar from '@/components/NavBar.vue'
import useProfileStore from '@/stores/profileStore'

const profileStore = useProfileStore()

onBeforeMount(() => {
  profileStore.getMe()
})
</script>

<template>
  <NavBar />
  <router-view />
</template>
