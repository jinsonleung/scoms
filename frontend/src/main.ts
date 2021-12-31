import { createApp, createVNode } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import "@/assets/css/main.css"  //引入全局CSS样式
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import dialogDrag from "@/utils/directives/dialogDrag"  //引入二将封装的可拖拽dialog组件
// import * as Icons from '@element-plus/icons'
import * as Icons from '@element-plus/icons-vue'

// 创建Icon组件
const Icon = (props: { icon: string }) => {
  const { icon } = props
  return createVNode(Icons[icon as keyof typeof Icons])
}

const app = createApp(App);
app.component('Icon', Icon) //注册Icon组件
app.use(router).use(store);
app.use(ElementPlus, {size: 'mini', zIndex:3000})  // ElementPlus组件全局配置为small样式
app.use(dialogDrag) //注册自定义可拖拽dialog组件
app.mount('#app');