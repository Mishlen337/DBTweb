import Vue from 'vue'
import App from './App.vue'

import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vueperslides/dist/vueperslides.css'

import router from './router'
import axios from 'axios'

// Set the base URL for your API
axios.defaults.baseURL = process.env.VUE_APP_API;

// Create a Vue prototype to make axios accessible globally within your Vue components


Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueperSlides)
Vue.use(VueperSlide)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

