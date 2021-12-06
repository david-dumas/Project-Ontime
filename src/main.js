import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import VueTextareaAutosize from 'vue-textarea-autosize';
import Vuex from 'vuex';
import store from '../src/store/store'

Vue.config.productionTip = false

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
