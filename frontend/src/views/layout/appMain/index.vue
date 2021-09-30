<!--
 * @Author: JinsonLiang
 * @Date: 2021-07-02 17:43:09
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-24 14:26:20
 * @Description: file content
 * @FilePath: \vue3-vite-ssis\src\views\layout\appMain\index.vue
-->

<template>
  <section class="app-main">
    <!-- 内部应该显示子路由页面信息 -->
    <router-view></router-view>
  </section>
</template>

<script lang="ts">
import { ref, defineComponent } from "vue";
export default defineComponent({
  name: "AppMain",
  setup() {
    const refData = ref(0);
    return {
      refData,
    };
  },
});
</script>
<style scoped>
    .app-main {
        /*50 = navbar  */
        min-height: calc(100vh - 50px);
        width: 100%;
        position: relative;
    }
</style>
