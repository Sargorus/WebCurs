import { createRouter, createWebHistory } from 'vue-router'

import MainPage from '@/pages/MainPage.vue'
import LoginPage from '@/pages/LoginPage.vue'

import GenresList from '@/components/GenresList.vue'
import GamesList from '@/components/GamesList.vue'
import GenreInGamesList from '@/components/GenreInGamesList.vue'
import GameSetsList from '@/components/GameSetsList.vue'
import GameOnSetsList from '@/components/GameOnSetsList.vue'
import HallsList from '@/components/HallsList.vue'
import OrdersList from '@/components/OrdersList.vue'
import OrderItemsList from '@/components/OrderItemsList.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass: 'active',
  routes: [
    { path: '/', name: 'main', component: MainPage },
    { path: '/login', name: 'login', component: LoginPage },

    { path: '/genres', name: 'genres', component: GenresList },
    { path: '/games', name: 'games', component: GamesList },
    { path: '/genre-in-games', name: 'genre-in-games', component: GenreInGamesList },
    { path: '/game-sets', name: 'game-sets', component: GameSetsList },
    { path: '/game-on-sets', name: 'game-on-sets', component: GameOnSetsList },
    { path: '/halls', name: 'halls', component: HallsList },
    { path: '/orders', name: 'orders', component: OrdersList },
    { path: '/order-items', name: 'order-items', component: OrderItemsList },
  ],
})

export default router
