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
    /* Navigation guard zodat gebruiker niet vanaf adresbalk de inlog kan omzeilen */
    beforeEnter: (to, from, next) => {
      
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
});

// Voordat de router de component laadt, wordt er gecontroleerd of de route een meta field heeft met requiresAuth.
router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (localStorage.getItem("token") == null) {
      next({
        //redirect naar login page als gebruiker geen token heeft
        path: "/",
        //relative url omzetten naar full url
        params: { nextUrl: to.fullPath },
      });
    } else {
      //redirect naar login page als er token is verlopen
      if (!store.state.isAuthenticated) {
        next({
          path: "/",
          //relative url omzetten naar full url
          params: { nextUrl: to.fullPath },
        });
      } else {
        next();
      }
    }
  } else {
    next();
  }
});








/* router.beforeEach((to, from, next) => {

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (isAuthenticated == true){
      next()
    }

  } 
  else {
    let redirect_url = this.$route.query.redirect || '/login'
    this.$router.push(redirect_url)
  }
  next()
}); */

export default router