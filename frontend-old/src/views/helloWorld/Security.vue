<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-24 15:27:30
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-24 15:27:31
 * @Description: 安全標準組件
 * @FilePath: \vue3-vite-ssis\src\views\helloWorld\Security.vue
-->

<template>
  <div class="app-container">
      <h1>這是安全標準組件</h1>
  </div>
</template>

<script lang='ts'>
import { ref, defineComponent } from "vue";
export default defineComponent({
  name: "Security",
  setup() {
    const refData = ref(0);
    return {
      refData
    };
  }
});
</script>
<style scoped>
</style>
