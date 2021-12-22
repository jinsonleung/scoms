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
<!--      <div class="toggle-button" @click="toggleSidebar">-->
        <Icon class="collapse-icon" :icon="isCollapse?'Expand':'Fold'" @click="toggleSidebar"></Icon>
<!--      </div>-->

      <div class="right">
      <el-popover
        placement="bottom"
        :width="320"
        trigger="click"
        popper-class="popper-user-box"
      >
        <template #reference>
          <div class="author">
            <i class="icon el-icon-s-custom" />
            {{ userInfo && userInfo.nickName || '' }}
            <i class="el-icon-caret-bottom" />
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
  //background-color: #fff;
  background-color: #bfffd9;

      //.toggle-button {
      //  line-height: 50px;
      //  height: 100%;
      //  float: left;
      //  cursor: pointer;
      //  transition: background 0.3s;
      //  align-content: center;
      //
      //  :hover {
      //    background: rgba(0, 0, 0, 0.025);
      //    display: inline-block;
      //  }
      //}
  //.header11 {
  //  height: 50px;
  //  line-height: 50px;
  //  box-shadow: 0 1px 4px rgb(0 21 41 / 8%);
  //  position: relative;
  //
  //  .toggle-button {
  //    line-height: 50px;
  //    height: 100%;
  //    float: left;
  //    cursor: pointer;
  //    transition: background 0.3s;
  //    align-content: center;
  //
  //    :hover {
  //      background: rgba(0, 0, 0, 0.025);
  //      display: inline-block;
  //    }
  //  }
  //}

  .collapse-icon {
    margin-left: 0px;
    height: 20px;
    width: 20px;
  }

  .is-active {
    transform: rotate(180deg);
  }
}

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
  .right > div > .icon{
    font-size: 18px;
    margin-right: 6px;
  }
  .author {
    margin-left: 10px;
    cursor: pointer;
  }
</style>
