/*
 * @Author: JinsonLiang
 * @Date: 2021-07-05 09:44:52
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-24 17:41:50
 * @Description: file content
 * @FilePath: \vue3-vite-ssis\src\router\index.ts
 */

import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import Login from "@/views/Login.vue";
import Index from "@/views/index.vue";
import TestAxios from "@/views/TestAxios.vue"
import Env from "@/views/env/index.vue"

const routes = [
  { //默认页面
    path: '/',
    redirect: '/home',
    name:'Home',
    component: ()=>import ('@/views/layout/index.vue'),
    children:[
      {
        path:'/home',
        name: 'Home',
        meta:{title:'首页'},
        component:()=>import('@/views/Home.vue'),
      },
      {
        path:'/dashboard',
        name: 'Dashboard',
        meta:{title:'仪表盘'},
        component:()=>import('@/views/Dashboard/dashboard.vue'),
      },
      {
        path:'/helloworld',
        name: 'HelloWorld',
        meta:{title:'世界你好'},
        component:()=>import('@/views/helloWorld/HelloWorld.vue'),
      },
      {
        path:'/security',
        name: 'Security',
        meta:{title:'安全'},
        component:()=>import('@/views/helloWorld/Security.vue'),
      },
      {
        path:'/stationsetting',
        name: 'StationSetting',
        meta:{title:'安全配置'},
        component:()=>import('@/views/stationSetting/StationSetting.vue'),
      },
      {
        path:'/securityaccident',
        name: 'SecurityAccident',
        meta:{title:'安全事故'},
        component:()=>import('@/views/security/SecurityAccident.vue'),
      },
      {
        path:'/vendorsetting',
        name: 'VendorSetting',
        meta:{title:'供应商配置'},
        component:()=>import('@/views/vendor/VendorSetting.vue'),
      },
      { //简介页面
        path: '/introduce',
        name: 'Introduce',
        meta:{title:'简介页面'},
        component: ()=>import('@/views/Introduce.vue'),
      },
      { //商品页面
        path: '/goodlist',
        name: 'GoodList',
        meta:{title:'商品页面'},
        component: ()=>import('@/views/GoodList.vue'),
      },
      { //axios测试页面
        path: '/testaxios',
        name: 'Testaxios',
        meta:{title:'axios测试页面'},
        component: ()=>import('@/views/TestAxios.vue'),
      },
      { //跨域请求测试
        path: '/crossdomain',
        name: 'CrossDomain',
        meta:{title:'跨域请求测试'},
        component: ()=>import('@/views/crossDomain/index.vue'),
      },
      { //获取环境变量页面
        path: '/env',
        name: 'Env',
        meta:{title:'环境变量'},
        component: ()=>import('@/views/env/index.vue'),
      },
      { //文字识别
        path: '/characterRecognition',
        name: 'CharacterRecognition',
        meta:{title:'文字识别'},
        component: ()=>import('@/views/characterRecognition/index3.vue'),
      },
      { //图片上传
        path: '/imageUpload',
        name: 'ImageUpload',
        meta:{title:'图片上传'},
        component: ()=>import('@/views/uploadImage/index6.vue'),
      },
      { //分页
        path: '/pagination',
        name: 'Pagination',
        meta:{title:'分页'},
        component: ()=>import('@/views/pagination/index.vue'),
      },
      { //多条件查询
        path: '/multisearch',
        name: 'MultiQuery',
        meta:{title:'多条件查询'},
        component: ()=>import('@/views/multiSearch/index.vue'),
      },
     { //基本表单
        path: '/baseform',
        name: 'BaseForm',
        meta:{title:'基本表单'},
        component: ()=>import('@/views/Test/BaseForm.vue'),
      },
     { //对话弹窗
        path: '/dialogform',
        name: 'DialogForm',
        meta:{title:'对话弹窗'},
        component: ()=>import('@/views/Test/dialogForm.vue'),
      },
    ]
  },
  { //登录页面
    path: '/login',
    name: 'Login',
    component: ()=>import('@/views/Login.vue')
  },
];

const router = createRouter({
  history: createWebHistory(),  //去掉url中的#號
  routes, // short for `routes: routes`
});


// 路由前置守卫
router.beforeEach(function (to, from, next) {
  // 你需要在跳转路由前做点啥
  next();           // next()函数为必须，在前置守卫结束的时候必须进行next来决定路由走向，不然会发生死循环
})

// 路由后置守卫
router.afterEach(() => {
  // 你需要做点啥，在跳转路由之后，这里不需要next()方法
})


export default router;
