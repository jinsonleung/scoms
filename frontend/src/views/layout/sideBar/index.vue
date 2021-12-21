<template>
  <div class="sidebar-container" :class="{'collapse-width': isCollapse}">
    <!--企业Logo-->
    <div class="logo" @click="$router.push('/')">
      <img class="logo-img" :src="logoSrc" alt="logo" />
      <transition name="el-zoom-in-center">
        <h1 v-show="opened" class="logo-text">{{systemTitle}}</h1>
      </transition>
    </div>
    <!--横线-->
    <div class="line"/>
    <!--左边菜单-->
    <el-scrollbar style="height: 100%; background-color: #222832">
      <el-menu
        class="el-menu-vertical"
        active-text-color="yellow"
        background-color="#222832"
        text-color="#fff"
        default-active="$route.path"
        router
        :collapse="isCollapse"
      >
        <el-menu-item index="/">
          <el-icon><home-filled/></el-icon>
          <span>首页</span>
        </el-menu-item>
        <el-menu-item index="/dashboard">
          <el-icon><icon-menu/></el-icon>
          <span>仪表盘</span>
        </el-menu-item>
        <!--1.安检系统-->
        <el-sub-menu index="1" disabled>
          <template #title>
            <el-icon><IconMenu /></el-icon>
            <span>安检系统</span>
          </template>
          <el-sub-menu index="1-1">
            <template #title>
            <el-icon><location /></el-icon>
            <span>场站管理</span>
            </template>
            <el-menu-item index="/stationsetting">场站信息配置</el-menu-item>
            <el-menu-item index="1-1-2">场站权配置</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="1-2">
            <template #title>
            <el-icon><location /></el-icon>
            <span>供应商管理</span>
            </template>
            <el-menu-item index="/vendorsetting">供应商采购</el-menu-item>
            <el-menu-item index="1-2-2">供应商服务</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="1-3">
            <template #title>
            <el-icon><location /></el-icon>
            <span>安全监控</span>
            </template>
            <el-menu-item index="/security">安全标准配置</el-menu-item>
            <el-menu-item index="/securityaccident">安全事项</el-menu-item>
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
            <span>组件测试</span>
          </template>
          <el-sub-menu index="2-1">
            <template #title>
            <el-icon><location /></el-icon>
            <span>跨域请求</span>
            </template>
            <el-menu-item index="/testaxios">Aciox测试</el-menu-item>
            <el-menu-item index="/crossdomain">跨域请求</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="2-2">
            <template #title>
            <el-icon><location /></el-icon>
            <span>表单测试</span>
            </template>
            <el-menu-item index="/baseform">基本表单</el-menu-item>
            <el-menu-item index="/dialogform">对话弹窗</el-menu-item>
          </el-sub-menu>

          <el-sub-menu index="2-3">
            <template #title>
            <el-icon><location /></el-icon>
            <span>其他组件</span>
            </template>
            <el-menu-item index="/introduce">简介页面</el-menu-item>
            <el-menu-item index="/goodlist">商品维护</el-menu-item>
            <el-menu-item index="/characterRecognition">文字识别</el-menu-item>
            <el-menu-item index="/imageUpload">图片上传</el-menu-item>
            <el-menu-item index="/pagination">分页</el-menu-item>
            <el-menu-item index="/multisearch">多条件查询</el-menu-item>
          </el-sub-menu>
        </el-sub-menu>

        <!--3.赛诚运营系统-->
        <el-sub-menu index="3">
          <template #title>
            <el-icon><IconMenu /></el-icon>
            <span>运营系统</span>
          </template>
        </el-sub-menu>

      </el-menu>
    </el-scrollbar>
  </div>
</template>

<script lang="ts">
import { defineComponent,reactive,computed,ref } from 'vue'
import { useRouter } from 'vue-router'
import { useStore, mapGetters, mapActions} from 'vuex'
import logoSrc from '@/assets/img/logo2.png'  //Logo图片
import {
  Expand,
  Bell,
  Location,
  Document,
  Menu as IconMenu,
  Setting,
  HomeFilled,
} from '@element-plus/icons'


export default defineComponent({
  components: {
    Expand,
    Bell,
    Location,
    Document,
    Setting,
    IconMenu,
    HomeFilled,
  },
  computed: { // Vuex全局状态
      ...mapGetters(['isCollapse'])
    },
  setup() {
    const router = useRouter()
    const systemTitle = ref('SCOMS') //系统名称
    const opened = ref(true)  // true:显示系统名称
    return {
      systemTitle,
      opened,
      logoSrc,
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
//调整图标与菜单名的间隔
.el-menu-item i, .el-sub-menu__title i {
  color: inherit;
  font-size: 16px;
  margin-right: 5px;
}

.logo {
  //position: absolute;
    display: flex;
    align-items: center;
    //justify-content: left;
    height: 50px;
    background-color: #222832;
  .logo-img {
    width: 32px;
    height: 32px;
    margin-left: 20px;
  }

  .logo-text {
    display: inline-block;
    height: 50px;
    margin-left: 12px;
    font-size: 16px;
    line-height: 50px;
    color: navajowhite;
  }

}
  .line {
    border-bottom: 0.5px solid #242f42;
  }
</style>
