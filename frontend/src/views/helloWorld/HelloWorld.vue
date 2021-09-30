<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-24 14:43:12
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-24 15:24:56
 * @Description: 父組件
 * @FilePath: \vue3-vite-ssis\src\views\helloWorld\HelloWorld.vue
-->

<template>
  <div class="app-container">
      <h1>這是Hello World父組件</h1> <br>
      姓名：{{state.name}}
      <hr>
      <!-- 第1個子組件 -->
      <son-1></son-1>
      <hr>
      <!-- 第2個子組件 -->
      <son @click="parentClick"></son>
  </div>
</template>

<script lang='ts'>
import { ref, reactive, defineComponent } from "vue"
import Son1 from "@/components/son1.vue"
import Son from "@/components/son.vue"

export default defineComponent({
  name: "HelloWorld",
  components: { Son1, Son },
  setup(prop, context) {
    const state = reactive({
        name: "這是來自父組件的劉一"
    })
    const parentClick=(e:string)=>{
        console.log("SON組件傳過來的值：",e)
    }
    return {
      state,
      parentClick
    };
  }
});
</script>
<style scoped>
</style>
