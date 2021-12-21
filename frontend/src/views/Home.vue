<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-30 11:28:05
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-09-04 12:37:13
 * @Description: 
 * @FilePath: \vue3-vite-ssis\src\views\Home.vue
-->

<template>
  <div class="home-view">
    <el-empty description="首页"/>
    <h2 class="title">{{ msg }}</h2>
  </div>
</template>

<script lang="ts">
import {ref, defineComponent, reactive, onMounted} from "vue";

export default defineComponent({
  name: "Home",
  setup() {
    const refData = ref(0)
    const msg = ref('Welcome to the management system！')
    const h2Style = reactive({
      color: '#435448'
    })
    return {
      refData,
      msg,
      h2Style
    };
  },
});


</script>

<style lang="scss" scoped>
.home-view {
  .title {
    color: #3e36ff;
    text-align: center;
  }
}
</style>
