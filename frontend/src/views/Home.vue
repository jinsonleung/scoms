<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-30 11:28:05
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-09-04 12:37:13
 * @Description: 
 * @FilePath: \vue3-vite-ssis\src\views\Home.vue
-->
<template>
  <div>==HOME PAGE==</div>
</template>

<script lang="ts">
import { ref, defineComponent } from "vue";
export default defineComponent({
  name: "App",
  setup() {
    const refData = ref(0);
    return {
      refData,
    };
  },
});
</script>
<style></style>
