import Vue from 'vue'
import VueRouter from 'vue-router'
import AppLayout from "@/components/layout/AppLayout.vue";


export default new VueRouter({
    routes: [
      { // 默认路由
        path: '/',
        redirect: '/home'
      },
      {
        path: '/home',
        component: AppLayout,
      }
    ]
  })

// Vue.use(VueRouter)