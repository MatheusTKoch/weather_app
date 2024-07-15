import { createRouter, createWebHistory } from 'vue-router'
import PesquisaView from '@/views/PesquisaView.vue'
import App from '@/App.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: App
    },
    {
      path: '/resultado/:cidade',
      name: 'Resultado',
      component: Resultado,
      props: true,
    }
  ]
})

export default router
