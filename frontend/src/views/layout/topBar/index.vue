<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-21 14:38:38
 * @LastEditors: JinsonLiang
 * @LastEditTime: 2021-08-28 11:05:07
 * @Description:
 * @FilePath: \vue3-vite-ssis\src\views\layout\topBar\index.vue
-->
<template>
  <div class="topbar-container">
    <div class="header">
      <div class="toggle-btn" @click="toggleSidebar">
        <i
          class="ri-indent-decrease ri-lg"
          :class="{ 'ri-indent-increase': isCollapse }"
        ></i>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { reactive, computed } from "vue";
import { useStore, mapGetters, mapActions } from "vuex";
export default {
  name: "index",
  computed: {
    ...mapGetters(["isCollapse"]), // 语法糖
  },
  setup(props, context) {
    const state = reactive({
      title: "场站安全系统",
    });

    const store = useStore();
    const isCollapse = computed(() => store.getters.isCollapse); //getters
    const toggleSidebar = () => store.dispatch("toggleSidebar", state.title); //actions

    const handleClick = () => {
      store.state.app.isCollapse = !store.state.app.isCollapse;
      console.log(store.state.app.isCollapse);
    };
    return {
      state,
      handleClick,
      // isCollapse,
      toggleSidebar,
      //...mapActions(['toggleSidebar']) // 语法糖
    };
  },
};
</script>

<style lang="scss" scoped>
.topbar-container {
  width: 100%;
  height: 50px;
  background-color: #fff;
  .header {
    height: 50px;
    line-height: 50px;
    box-shadow: 0 1px 4px rgb(0 21 41 / 8%);
    position: relative;
    .toggle-btn {
      line-height: 50px;
      height: 100%;
      float: left;
      cursor: pointer;
      transition: background 0.3s;
      :hover {
        background: rgba(0, 0, 0, 0.025);
        display: inline-block;
      }
    }
  }
  .is-active {
    transform: rotate(180deg);
  }
}
</style>
