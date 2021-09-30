<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-24 14:32:38
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-24 15:21:48
 * @Description: 子組件
 * @FilePath: \vue3-vite-ssis\src\components\son.vue
-->

<template>
  <div class="app-container">
      <el-button @click="handleSonClick">這是子組件SON的按鈕</el-button>
  </div>
</template>

<script lang='ts'>
import { ref, defineComponent, reactive } from "vue";
export default defineComponent({
  name: "Son",
  setup(props, context) {
    const state = reactive({
        name: "這是來自SON組件的張三"
    })
    const handleSonClick = ()=>{
        console.log(state.name)
        context.emit('parentClick', state.name)    //向父組件傳值
    }
    return {
      state,
      handleSonClick
    };
  }
});
</script>
<style scoped>
</style>
