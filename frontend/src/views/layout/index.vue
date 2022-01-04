<template>
  <div>
    <!--1）左边菜单栏-->
    <side-bar></side-bar>
    <!--2）右边内容栏（包括头部、内容部及脚部）-->
      <!--折叠/展开状态-->
      <div class="right-container" :class="{'collapse-ml': collapse}">
        <top-bar></top-bar>
        <top-tags></top-tags>
        <app-main></app-main>
        <foot-bar></foot-bar>
      </div>
  </div>
</template>

<script>
import {ref, defineComponent} from "vue"
import {mapGetters} from 'vuex'
import SideBar from "@/views/layout/sideBar/index.vue"
import TopBar from "@/views/layout/topBar/index.vue"
import TopTags from "@/views/layout/topTags/index.vue"
import AppMain from "@/views/layout/appMain/index.vue"
import FootBar from '@/views/layout/footBar/index.vue'

export default defineComponent({
  name: "Layout",
  components: {SideBar, TopBar, TopTags, AppMain, FootBar},
  computed: {
    ...mapGetters(['collapse'])
  },
  setup() {
    const refData = ref(0);
    return {
      refData,
    };
  },
});
</script>
<style lang="scss" scoped>
.right-container {
  //background-color: dodgerblue;
  width: calc(100% - 210px);
  height: 100%;
  margin-left: 210px;
  transition: 0.3s;
}

.collapse-ml {
  width: calc(100% - 64px);
  margin-left: 64px;
  transition: 0.28s;
}
</style>
