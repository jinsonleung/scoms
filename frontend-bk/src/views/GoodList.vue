<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-24 17:40:54
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-30 14:01:35
 * @Description: 商品列表
 * @FilePath: \vue3-vite-ssis\src\views\GoodList.vue
-->

<template>
  <!-- 商品列表 -->
  <list></list>
</template>

<script lang='ts'>
import { ref, defineComponent, onMounted } from "vue"
import List from '@/components/goods/List.vue'

export default defineComponent({
  name: "GoodList",
  components: { List },
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


