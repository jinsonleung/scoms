<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-24 14:33:03
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-24 15:16:27
 * @Description: 子組件Son1
 * @FilePath: \vue3-vite-ssis\src\components\son1.vue
-->

<template>
  <div class="app-container">
      <el-button @click="handleClick">這是子組件SON1的按鈕</el-button>
      <h2>SON1的姓名：{{title}}</h2>
  </div>
</template>

<script lang='ts'>
import { ref, defineComponent } from "vue";
export default defineComponent({
  name: "Son1",
  props: {
      title: String,    //接受父組件傳過來的參數
  },
  setup(props,context) {    //setup()第1個參數是props,第2個參數是context
    const handleClick=()=>{
        console.log("父組件轉過來的值是：",props.title)
        console.log("props:", props)
        console.log("context:", context)
    }
    return {
      handleClick
    };
  }
});
</script>
<style scoped>
</style>
