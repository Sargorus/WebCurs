import { defineStore } from 'pinia'
import api from '@/api'

const useProfileStore = defineStore('profile', {
  state: () => ({
    user: null,
    loading: false,
    error: '',
  }),

  getters: {
    isAuthenticated: (state) => !!state.user,
    userName: (state) => (state.user ? state.user.username : 'гость'),
  },

  actions: {
    async getMe() {
      this.loading = true
      try {
        const { data } = await api.get('/profile/me/')
        this.user = data.user ?? null
        this.error = ''
      } catch (e) {
        this.user = null
      } finally {
        this.loading = false
      }
    },

    async login(username, password) {
      this.loading = true
      this.error = ''
      try {
        const { data } = await api.post('/profile/login/', { username, password })
        this.user = data.user ?? null
        return true
      } catch (e) {
        this.user = null
        this.error = e.response?.data?.detail ?? 'Не удалось войти'
        return false
      } finally {
        this.loading = false
      }
    },

    async logout() {
      try {
        await api.post('/profile/logout/')
      } catch (e) {
        // игнорируем ошибки выхода — состояние всё равно сбрасываем
      } finally {
        this.user = null
      }
    },
  },
})

export default useProfileStore
