import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import VueTextareaAutosize from 'vue-textarea-autosize';
import store from '../src/store/store'

Vue.use(store)

Vue.use(VueTextareaAutosize)

Vue.config.productionTip = false

new Vue({
  //router toevoegen aan app
  router,
  //store toevoegen aan app
  store,
  //vuetify toevoegen aan app
  vuetify,
  render: h => h(App)
}).$mount('#app')
