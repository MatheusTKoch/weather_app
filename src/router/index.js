import { createRouter, createWebHistory } from 'vue-router'
import App from '@/App.vue'
import Resultados from '@/components/Resultados.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Menu',
      component: App,
    },
    {
      path: '/weather_app/resultado/:cidade',
      name: 'Resultado',
      component: Resultados,
      props: true,
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.name === 'Resultado' && !from.name === null) {
    next({ name: 'Menu'});
  } else {
    next();
  }
})

export default router
