<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-24 15:35:52
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-24 15:37:49
 * @Description: 
 * @FilePath: \vue3-vite-ssis\src\views\security\SecurityAccident.vue
-->
<template>
  <div class="app-container">
      <h1>==安全事故==</h1>
  </div>
</template>

<script lang='ts'>
import { ref, defineComponent } from "vue";
export default defineComponent({
  name: "SecuritySetting",
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