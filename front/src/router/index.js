import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: () => import('@/views/HomePage.vue')
    },
    {
      path:'/pageone',
      name:'pageone',
      component:()=>import('@/views/pageone.vue'),
    }

  ]
})

export default router
