<!--
 * @Author: JinsonLiang
 * @Date: 2021-07-02 17:43:09
 * @LastEditors: JinsonLiang
 * @LastEditTime: 2021-08-12 11:43:58
 * @Description: file content
 * @FilePath: \vue3-vite-ssis\src\views\index1.vue
-->

<template>
  <div>
    <h1>==INDEX PAGE==</h1>
    <hr />
  </div>
</template>

<script lang="ts">
import { log } from "util";
import { ref, defineComponent } from "vue";

export default defineComponent({
  name: "Index",
  setup() {
    const refData = ref(0);
    return {
      refData,
    };
  },
});
</script>
<style scoped lang="scss">
h1 {
  color: darkviolet;
}
</style>
