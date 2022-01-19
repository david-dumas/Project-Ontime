import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import VueTextareaAutosize from "vue-textarea-autosize";
import Vuex from "vuex";
import store from "../src/store/store";
import firebase from "firebase/compat/app";
import "firebase/compat/firestore";

Vue.config.productionTip = false;

firebase.initializeApp({
  apiKey: "AIzaSyDexrUVD7j9oLV-ryO8FMX6yFXvX9PxEKY",
  authDomain: "ontime-b24b0.firebaseapp.com",
  databaseURL:
    "https://ontime-b24b0-default-rtdb.europe-west1.firebasedatabase.app/",
  projectId: "ontime-b24b0",
  storageBucket: "ontime-b24b0.appspot.com",
  messagingSenderId: "461960083217",
  appId: "1:461960083217:web:7359152142ff374204feb0",
});

export const db = firebase.firestore();

Vue.use(Vuex);

Vue.use(VueTextareaAutosize);

new Vue({
  //router toevoegen aan app
  router,
  //store toevoegen aan app
  store,
  //vuetify toevoegen aan app
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
