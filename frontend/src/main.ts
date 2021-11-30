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

app.use(router).use(store);
// ElementPlus全局配置https://element-plus.gitee.io/zh-CN/guide/quickstart.html#%E5%85%A8%E5%B1%80%E9%85%8D%E7%BD%AE
app.use(ElementPlus, {size: 'small', zIndex:3000})  // ElementPlus组件全局配置为small样式
app.mount('#app');