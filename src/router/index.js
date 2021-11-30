import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login';
import Bdashboard from '../views/Bdashboard';
import Adashboard from '../views/Adashboard';
import Agenda from '../views/Agenda';
import Help from '../views/Help';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/begeleider-dashboard',
    name: 'Bdashboard',
    component: Bdashboard,
    /* protected route aanmaken zodat gebruiker niet vanaf adresbalk de inlog kan omzeilen */
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/admin-dashboard',
    name: 'Adashboard',
    component: Adashboard,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/agenda',
    name: 'Agenda',
    component: Agenda,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/help',
    name: 'Help',
    component: Help
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router