<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-24 15:35:52
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-24 15:35:53
 * @Description: 
 * @FilePath: \vue3-vite-ssis\src\views\vendor\VendorSetting.vue
-->
<template>
  <div class="app-container">
      <h1>==供應商設置==</h1>
  </div>
</template>

<script lang='ts'>
import { ref, defineComponent } from "vue";
export default defineComponent({
  name: "VendorSetting",
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