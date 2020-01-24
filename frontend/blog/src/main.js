import Vue from 'vue';
import VueSession from 'vue-session';
// eslint-disable-next-line import/extensions
import App from './App.vue';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';
import 'material-design-icons-iconfont/dist/material-design-icons.css';


Vue.config.productionTip = false;
Vue.use(VueSession);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
}).$mount('#app');
