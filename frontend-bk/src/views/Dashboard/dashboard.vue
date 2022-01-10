<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-24 11:45:25
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-24 11:51:59
 * @Description: 仪表盘
 * @FilePath: \vue3-vite-ssis\src\views\Dashboard\dashboard.vue
-->

<template>
  <div class="app-container">Dashboard</div>
  <Icon icon="Edit"></Icon>
</template>

<script lang='ts'>
import { ref, defineComponent } from "vue";
export default defineComponent({
  name: "Dashboard",
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
