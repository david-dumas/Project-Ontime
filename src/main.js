import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import VueTextareaAutosize from 'vue-textarea-autosize';
import Vuex from 'vuex';
import store from '../src/store/store'
import firebase from "firebase/compat/app";
import "firebase/compat/firestore";

Vue.config.productionTip = false;

firebase.initializeApp({
  apiKey: "AIzaSyBrZtMu6iplR861j3q1ELyagZIgpWGDeHI",
  authDomain: "ontime-4931c.firebaseapp.com",
  projectId: "ontime-4931c",
  storageBucket: "ontime-4931c.appspot.com",
  messagingSenderId: "390425882655",
  appId: "1:390425882655:web:31c5afd6a5cd90b876a52a",
});

export const db = firebase.firestore();

Vue.use(Vuex);

Vue.use(VueTextareaAutosize)

new Vue({
  //router toevoegen aan app
  router,
  //store toevoegen aan app
  store,
  //vuetify toevoegen aan app
  vuetify,
  render: h => h(App)
}).$mount('#app')
