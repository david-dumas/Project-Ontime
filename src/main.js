import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import firebase from "firebase/compat/app";
import VueTextareaAutosize from 'vue-textarea-autosize';
import 'firebase/compat/firestore';
import store from '../src/store/store'

Vue.use(store)

Vue.use(VueTextareaAutosize)

Vue.config.productionTip = false

firebase.initializeApp({
  apiKey: "AIzaSyACLnGk_CCr8-23vkGA3SurCIHcSSjmsY0",
  authDomain: "vue-calendar-b5a51.firebaseapp.com",
  projectId: "vue-calendar-b5a51",
  storageBucket: "vue-calendar-b5a51.appspot.com",
  messagingSenderId: "16826968433",
  appId: "1:16826968433:web:00771685c2d6ac6cd96ed0"
});

export const db = firebase.firestore();

new Vue({
  //router toevoegen aan app
  router,
  //store toevoegen aan app
  store,
  //vuetify toevoegen aan app
  vuetify,
  render: h => h(App)
}).$mount('#app')
