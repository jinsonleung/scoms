// import { createApp } from 'vue'
// import App from './App.vue'
//
// createApp(App).mount('#app')



import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import store from './store'
import axios from "axios" //引入axios
import '@/styles/index.scss'    //引入scss
import '@/styles/fonts/remixicon.css' //引入icon


const app = createApp(App);
//全局axios
// app.config.globalProperties.$axios = axios;

app.use(router).use(ElementPlus).use(store);
app.mount('#app');