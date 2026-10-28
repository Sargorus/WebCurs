<script setup>
const menu = [
  { to: '/genres', title: 'Жанры', description: 'CRUD модели Genre' },
  { to: '/games', title: 'Игры', description: 'CRUD модели Game' },
  { to: '/genre-in-games', title: 'Жанры в играх', description: 'CRUD модели GenreInGame' },
  { to: '/game-sets', title: 'Игровые наборы', description: 'CRUD модели GameSet' },
  { to: '/game-on-sets', title: 'Игры на наборах', description: 'CRUD модели GameOnSet' },
  { to: '/halls', title: 'Залы', description: 'CRUD модели Hall' },
  { to: '/orders', title: 'Заказы', description: 'CRUD модели Order' },
  { to: '/order-items', title: 'Позиции заказов', description: 'CRUD модели OrderItem' },
]
</script>

<template>
  <div class="container">

    <h1 class="mb-4">Главная страница</h1>

    <div class="row g-3">
      <div v-for="item in menu" :key="item.to" class="col-12 col-md-6 col-lg-4">
        <router-link :to="item.to" class="text-decoration-none">
          <div class="card h-100">
            <div class="card-body">

              <h5 class="card-title">{{ item.title }}</h5>
              <p class="card-text text-muted mb-0">{{ item.description }}</p>

            </div>
          </div>
        </router-link>
      </div>
    </div>

  </div>
</template>
