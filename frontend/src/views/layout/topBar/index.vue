<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-21 14:38:38
 * @LastEditors: JinsonLiang
 * @LastEditTime: 2021-08-28 11:05:07
 * @Description:
 * @FilePath: \vue3-vite-ssis\src\views\layout\topBar\index1.vue
-->
<template>
  <div class="top-bar-container">
    <div class="header">
      <div class="toggle-button" @click="toggleSidebar">
        <!--切换折叠/展开-->
        <Icon class="collapse-icon" :icon="isCollapse?'Expand':'Fold'"></Icon>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {ref, reactive, computed} from "vue";
import {useStore, mapGetters, mapActions} from "vuex";

export default {
  name: "index",
  computed: {
    ...mapGetters(["isCollapse"]), // 语法糖
  },
  setup(props: any, context: any) {
    const store = useStore()
    // const isCollapse = computed(() => store.getters.isCollapse); //getters
    const toggleSidebar = () => { //isCollapse状态
      store.dispatch("toggleSidebar", '折叠/展开') //actions, 第2个参数可以是随便字符串
      // iconName.value = isCollapse.value? 'Expand': 'Fold' //切换折叠/展开图标
    }
    return {
      toggleSidebar,
      // ...mapActions(['toggleSidebar']) // 语法糖
    };
  },
};
</script>

<style lang="scss" scoped>
.top-bar-container {
  width: 100%;
  height: 50px;
  background-color: #fff;
  .header {
    height: 50px;
    line-height: 50px;
    box-shadow: 0 1px 4px rgb(0 21 41 / 8%);
    position: relative;
    .toggle-button {
      line-height: 50px;
      height: 100%;
      float: left;
      cursor: pointer;
      transition: background 0.3s;
      align-content: center;
      :hover {
        background: rgba(0, 0, 0, 0.025);
        display: inline-block;
      }
    }
  }
  .collapse-icon {
    margin-left: 5px;
    height: 20px;
    width: 20px;
  }

  .is-active {
    transform: rotate(180deg);
  }
}
</style>
