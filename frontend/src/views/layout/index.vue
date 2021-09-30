<!--
 * @Author: JinsonLiang
 * @Date: 2021-07-02 17:43:09
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-24 11:38:09
 * @Description: file content
 * @FilePath: \vue3-vite-ssis\src\views\layout\index.vue
-->

<template>
  <div>
    <!-- <side-bar></side-bar>
    <top-bar></top-bar>
    <app-main></app-main>
    <foot-bar></foot-bar> -->
     <side-bar></side-bar>
    <div class="right-container" :class="{'collapse-ml': isCollapse}">
        <top-bar></top-bar>
        <app-main></app-main>
        <foot-bar></foot-bar>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, defineComponent } from "vue"
import { mapGetters } from 'vuex'
import SideBar from "@/views/layout/sideBar/index.vue"
import TopBar from "@/views/layout/topBar/index.vue"
import AppMain from "@/views/layout/appMain/index.vue"
import FootBar from '@/views/layout/footBar/index.vue'

export default defineComponent({
  name: "Layout",
  components: { SideBar, TopBar, AppMain, FootBar },
  computed:{
    ...mapGetters(['isCollapse'])
  },
  setup() {
    const refData = ref(0);
    return {
      refData,
    };
  },
});
</script>
<style lang="scss" scoped >
    .right-container{
        width: calc(100% - 210px);
        height: 100%;
        margin-left: 210px;
        transition: 0.3s;
    }
    .collapse-ml{
        width: calc(100% - 64px);
        margin-left: 64px;
        transition: 0.28s;
    }
</style>
