/*
 * @Author: JinsonLiang
 * @Date: 2021-07-05 09:33:33
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-21 16:01:18
 * @Description: file content
 * @FilePath: \vue3-vite-ssis\src\store\index.ts
 */
import {createStore} from "vuex"
import app from '@/store/modules/app'
import topTags from '@/store/modules/topTags'
import system from '@/store/modules/system'

// Create a new store instance.
const store = createStore({
    modules: {
      app,
      //topTags,  //顶部菜单标签栏
      system,
    },
    // 单独模块引入，每个模块都有单独的state，getters，actions， mutations
    // state,  共同维护的一个状态，state里面可以是很多个全局状态
    // getters, 获取数据并渲染
    // actions, 数据的异步操作，操作复杂的逻辑。
    // mutations 处理数据的唯一途径，state的改变或赋值只能在这里

  })

  export default store;

