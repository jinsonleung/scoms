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
      <!--切换折叠/展开-->
      <div class="left">
        <Icon class="collapse-icon" :icon="isCollapse?'Expand':'Fold'" @click="toggleSidebar"></Icon>
<!--        <span style="font-size: 20px">{{ name }}</span>-->
      </div>
      <div class="right">
        <el-popover
            placement="bottom"
            :width="320"
            trigger="click"
            popper-class="popper-user-box"
        >
          <template #reference>
            <div class="author">
              <i class="icon el-icon-s-custom"/>
              {{ userInfo && userInfo.nickName || '' }}
              <i class="el-icon-caret-bottom"/>
            </div>
          </template>
          <div class="nickname">
            <p>登录名：{{ userInfo && userInfo.loginUserName || '' }}</p>
            <p>昵称：{{ userInfo && userInfo.nickName || '' }}</p>
            <el-tag size="small" effect="dark" class="logout" @click="logout">退出</el-tag>
          </div>
        </el-popover>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {ref, toRefs, reactive, computed, defineComponent} from "vue";
import {useStore, mapGetters, mapActions} from "vuex";

export default defineComponent({
  name: "index",
  computed: {
    ...mapGetters(["isCollapse"]), // 语法糖
  },
  setup(props: any, context: any) {
    const state = reactive({
      name: 'aaa',
      userInfo: null,
      hasBack: false
    })
    const store = useStore()
    // const isCollapse = computed(() => store.getters.isCollapse); //getters
    const toggleSidebar = () => { //isCollapse状态
      store.dispatch("toggleSidebar", '折叠/展开') //actions, 第2个参数可以是随便字符串
      // iconName.value = isCollapse.value? 'Expand': 'Fold' //切换折叠/展开图标
    }
    return {
      ...toRefs(state),
      toggleSidebar,
      // ...mapActions(['toggleSidebar']) // 语法糖
    };
  },
});
</script>

<style scoped>
.header {
  height: 50px;
  border-bottom: 1px solid #e9e9e9;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 10px;
}

.el-icon-back {
  border: 1px solid #e9e9e9;
  padding: 4px;
  border-radius: 50px;
  margin-right: 10px;
}

.left .collapse-icon {
  height: 20px;
  width: 20px;
}

.right > div > .icon {
  font-size: 18px;
  margin-right: 6px;
}

.author {
  margin-left: 10px;
  cursor: pointer;
}
</style>
<style>
.popper-user-box {
  background: url('https://s.yezgea02.com/lingling-h5/static/account-banner-bg.png') 50% 50% no-repeat !important;
  background-size: cover !important;
  border-radius: 0 !important;
}

.popper-user-box .nickname {
  position: relative;
  color: #ffffff;
}

.popper-user-box .nickname .logout {
  position: absolute;
  right: 0;
  top: 0;
  cursor: pointer;
}
</style>