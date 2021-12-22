<!--
 * @Author: JinsonLiang
 * @Date: 2021-07-02 17:43:09
 * @LastEditors: JinsonLiang
 * @LastEditTime: 2021-08-28 11:10:56
 * @Description: file content
 * @FilePath: \vue3-vite-ssis\src\views\layout\footBar\index1.vue
-->

<template>
  <div class="footer">
    <div class="left">Copyright © 2019-2021 十三. All rights reserved.</div>
    <div class="right">
      <a target="_blank" href="https://github.com/newbee-ltd/vue3-admin">vue3-admin Version 3.0.0</a>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, defineComponent } from "vue";
export default defineComponent({
  name: "FootBar",
  setup() {
    const refData = ref(0);
    return {
      refData,
    };
  },
});
</script>
<style lang="scss" scoped>
  .footer {
    height: 30px;
    border-top: 1px solid #e9e9e9;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
  }
</style>
