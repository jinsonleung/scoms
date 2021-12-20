<template>
  <div class="sidebar-container" :class="{'collapse-width': isCollapse}">
    <!--企业Logo-->
    <div class="logo" @click="$router.push('/')">
      <img class="logo-img" :src="logoSrc" alt="logo" />
      <transition name="el-zoom-in-center">
        <h1 v-show="opened" class="logo-text">SCOMS</h1>
      </transition>
    </div>
    <div class="line"/>
      <!--左边菜单-->
      <el-menu
        class="el-menu-vertical-demo"
        active-text-color="red"
        background-color="#222832"
        text-color="#fff"
        default-active="$route.path"
        router
      >
        <!--1.检系统-->
        <el-sub-menu index="1">
          <template #title>
            <el-icon><IconMenu /></el-icon>
            <span>安检系统</span>
          </template>
          <el-sub-menu index="1-1">
            <template #title>
            <el-icon><location /></el-icon>
            <span>场站管理</span>
            </template>
            <el-menu-item index="/1-1-1">场站信息配置</el-menu-item>
            <el-menu-item index="1-1-2">场站权配置</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="1-2">
            <template #title>
            <el-icon><location /></el-icon>
            <span>供应商管理</span>
            </template>
            <el-menu-item index="1-2-1">供应商采购</el-menu-item>
            <el-menu-item index="1-2-2">供应商服务</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="1-3">
            <template #title>
            <el-icon><location /></el-icon>
            <span>安全监控</span>
            </template>
            <el-menu-item index="1-3-1">安全标准配置</el-menu-item>
            <el-menu-item index="1-3-2">安全事项</el-menu-item>
          </el-sub-menu>
          <el-menu-item-group title="设备测试">
            <el-menu-item index="1-4">设备使用</el-menu-item>
            <el-menu-item index="1-5">设备测试</el-menu-item>
          </el-menu-item-group>
          <el-sub-menu index="1-6" disabled> <!--不可使用-->
            <template #title>
            <el-icon><location /></el-icon>
            <span>人员管理</span>
            </template>
            <el-menu-item index="1-6-1">外出管理</el-menu-item>
            <el-menu-item index="1-6-2">差旅管理</el-menu-item>
          </el-sub-menu>
          <el-menu-item index="4">
          <el-icon><setting /></el-icon>
          <span>权限配置</span>
          </el-menu-item>
        </el-sub-menu>

        <!--2.测试系统-->
        <el-sub-menu index="2">
          <template #title>
            <el-icon><IconMenu /></el-icon>
            <span>测试系统</span>
          </template>
          <el-sub-menu index="2-1">
            <template #title>
            <el-icon><location /></el-icon>
            <span>跨域请求</span>
            </template>
            <el-menu-item index="2-1-1">Aciox测试</el-menu-item>
            <el-menu-item index="2-1-2">跨域请求</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="2-2">
            <template #title>
            <el-icon><location /></el-icon>
            <span>表单</span>
            </template>
            <el-menu-item index="/baseform">基本表单</el-menu-item>
            <el-menu-item index="/dialogform">对话弹窗</el-menu-item>
          </el-sub-menu>

          <el-menu-item index="2-3">
            <el-icon><bell /></el-icon>
            <span>简介页面</span>
          </el-menu-item>
          <el-menu-item index="2-4">
            <el-icon><bell /></el-icon>
            <span>商品维护</span>
          </el-menu-item>
          <el-menu-item index="2-5">
            <el-icon><bell /></el-icon>
            <span>文字识别</span>
          </el-menu-item>
          <el-menu-item index="2-6">
            <el-icon><bell /></el-icon>
            <span>图片上传</span>
          </el-menu-item>
          <el-menu-item index="2-7">
            <el-icon><bell /></el-icon>
            <span>分页</span>
          </el-menu-item>
          <el-menu-item index="2-8">
            <el-icon><bell /></el-icon>
            <span>多条件查询</span>
          </el-menu-item>

        </el-sub-menu>

        <!--3.赛诚运营系统-->
        <el-sub-menu index="3">
          <template #title>
            <el-icon><IconMenu /></el-icon>
            <span>运营系统</span>
          </template>
        </el-sub-menu>

      </el-menu>
  </div>
</template>

<script lang="ts">
import { defineComponent,reactive,computed,ref } from 'vue'
import { useRouter } from 'vue-router'
import {useStore, mapGetters, mapActions} from 'vuex'
import logoSrc from '@/assets/img/vueLogo.png'
import {
  Bell,
  Location,
  Document,
  Menu as IconMenu,
  Setting,
} from '@element-plus/icons'


export default defineComponent({
  components: {
    Bell,
    Location,
    Document,
    Setting,
    IconMenu,
  },
  computed: {
      ...mapGetters(['isCollapse'])
    },
  setup() {
    const router = useRouter()
    const opened = ref(true)
    return {
      opened,
      logoSrc,
      // handleOpen,
      // handleClose,
    }
  },
})
</script>


<style lang="scss" scoped>
.collapse-width {
  width: 64px !important;

}

.sidebar-container {
  width: 210px;
  height: 100%;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  transition: width 0.3s;
  z-index: 1001;
  overflow: hidden;

  .el-menu-vertical:not(.el-menu--collapse) {
    width: 210px;
  }

  .el-menu {
    border: none;
    height: 100%;
    width: 100% !important;
    overflow-y: auto;
  }
}

.el-menu-item, .el-submenu {
  text-align: left;
}

.el-menu-item i, .el-submenu__title i {
  color: inherit;
  font-size: 16px;
  margin-right: 5px;

}

.logo {
  //position: absolute;
  //top: 0;
  //display: flex;
  //width: 100%;
  //height: 50px;
  //overflow: hidden;
  //text-align: center;
  //cursor: pointer;
  //background-color: #2b2f3a;
  //justify-content: center;
  //align-items: center;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 50px;
    background-color: #222832;
  .logo-img {
    width: 32px;
    height: 32px;
  }

  .logo-text {
    display: inline-block;
    height: 50px;
    margin-left: 12px;
    font-size: 14px;
    line-height: 50px;
    color: red;
  }

}
  .line {
    //border-top: 0.5px solid hsla(0,0%,100%,.05);
    //border-bottom: 0.5px solid rgba(0,0,0,.2);
    border-bottom: 0.5px solid #5b5b5b;
  }
</style>
