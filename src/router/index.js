import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login';
import Bdashboard from '../views/Bdashboard';
import Adashboard from '../views/Adashboard';
import Agenda from '../views/Agenda';
import store from '../store/store';
import AdminLogin from '../views/AdminLogin';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/admin-login',
    name: 'AdminLogin',
    component: AdminLogin,
  },
  {
    path: '/begeleider-dashboard',
    name: 'Bdashboard',
    component: Bdashboard,
    beforeEnter: (to, from, next) => {
      if (store.state.isAuthenticated == false) {
        next('/');
      } if (localStorage.getItem("token") == null) {
        next('/');
      } else {
        next();
      }
    },
  },
  {
    path: '/admin-dashboard',
    name: 'Adashboard',
    component: Adashboard,
    beforeEnter: (to, from, next) => {
      if (store.state.isAuthenticated == false) {
        next('/');
      } if (localStorage.getItem("token") == null) {
        next('/');
      } else {
        next();
      }
    },
  },
  {
    path: '/agenda',
    name: 'Agenda',
    component: Agenda,
    beforeEnter: (to, from, next) => {
      if (store.state.isAuthenticated == false) {
        next('/');
      } if (localStorage.getItem("token") == null) {
        next('/');
      } else {
        next();
      }
    },
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router