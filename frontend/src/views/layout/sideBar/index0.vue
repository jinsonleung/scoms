<!--
 * @Author: Jinson.Liang
 * @Date: 2021-08-21 14:38:45
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-24 17:42:19
 * @Description: 左邊菜單欄
 * @FilePath: \vue3-vite-ssis\src\views\layout\sideBar\index1.vue
-->

<template>
  <div class="sidebar-container" :class="{'collapse-width': isCollapse}">
    <el-menu
        :default-active="$route.path"
        class="el-menu-vertical-demo"
        background-color="#304156"
        text-color="rgb(200 212 226)"
        router
        :collapse="isCollapse"
    >

      <el-menu-item index="/dashboard">
        <i class="ri-palette-line"></i>
        <template #title>仪表盘</template>
      </el-menu-item>

      <el-submenu index>
        <template #title>
          <i class="ri-file-text-line"></i>
          <span>安全监控</span>
        </template>
        <el-menu-item index="/helloworld">
          <i class="ri-secure-payment-line"></i>
          <template #title>安全事项</template>
        </el-menu-item>
        <el-menu-item index="/security">
          <i class="ri-coupon-5-line"></i>
          <template #title>安全标准</template>
        </el-menu-item>
      </el-submenu>
      <el-menu-item index="/stationsetting">
        <i class="ri-pencil-line"></i>
        <template #title>场站设置</template>
      </el-menu-item>

      <el-menu-item index="/vendorsetting">
        <i class="ri-discuss-line"></i>
        <template #title>供应商设置</template>
      </el-menu-item>

      <el-menu-item index="/securityaccident">
        <i class="ri-briefcase-4-line"></i>
        <template #title>安全事故</template>
      </el-menu-item>

      <el-menu-item index="/testaxios">
        <i class="ri-cactus-fill"></i>
        <template #title>Aciox测试</template>
      </el-menu-item>
      <el-menu-item index="/crossdomain">
        <i class="ri-cactus-fill"></i>
        <template #title>跨域请求</template>
      </el-menu-item>
      <el-menu-item index="/env">
        <i class="ri-haze-fill"></i>
        <template #title>环境变量</template>
      </el-menu-item>

      <el-menu-item index="/introduce">
        <i class="ri-user-voice-line"></i>
        <template #title>简介页面</template>
      </el-menu-item>
      <el-menu-item index="/goodlist">
        <i class="ri-shopping-bag-2-fill"></i>
        <template #title>商品维护</template>
      </el-menu-item>
      <el-menu-item index="/characterRecognition">
        <i class="ri-shopping-bag-2-fill"></i>
        <template #title>文字识别</template>
      </el-menu-item>
      <el-menu-item index="/imageUpload">
        <i class="ri-shopping-bag-2-fill"></i>
        <template #title>图片上传</template>
      </el-menu-item>
      <el-menu-item index="/pagination">
        <i class="ri-shopping-bag-2-fill"></i>
        <template #title>分页</template>
      </el-menu-item>
      <el-menu-item index="/multisearch">
        <i class="ri-search-2-fill"></i>
        <template #title>多条件查询</template>
      </el-menu-item>
      <el-menu-item index="/baseform">
        <i class="ri-search-2-fill"></i>
        <template #title>基本表单</template>
      </el-menu-item>

    </el-menu>
  </div>
</template>

<script>
import {reactive, computed} from 'vue'
import {useStore, mapGetters, mapActions} from 'vuex'

export default {
  name: 'siderBar',
  computed: {
    ...mapGetters(['isCollapse'])
  },
}
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


</style>
