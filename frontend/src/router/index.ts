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
    redirect: '/dashboard',
    name:'Dashboard',
    component: ()=>import ('@/views/layout/index.vue'),
    children:[
      {
        path:'/home',
        name: 'Home',
        component:()=>import('@/views/Home.vue'),
        meta:{title:'home'}
      },
      {
        path:'/dashboard',
        name: 'Dashboard',
        component:()=>import('@/views/Dashboard/dashboard.vue'),
        meta:{title:'dashboard'}
      },
      {
        path:'/helloworld',
        name: 'HelloWorld',
        component:()=>import('@/views/helloWorld/HelloWorld.vue'),
        meta:{title:'helloworld'}
      },
      {
        path:'/security',
        name: 'Security',
        component:()=>import('@/views/helloWorld/Security.vue'),
        meta:{title:'security'}
      },
      {
        path:'/stationsetting',
        name: 'StationSetting',
        component:()=>import('@/views/stationSetting/StationSetting.vue'),
        meta:{title:'stationsetting'}
      },
      {
        path:'/securityaccident',
        name: 'SecurityAccident',
        component:()=>import('@/views/security/SecurityAccident.vue'),
        meta:{title:'securityaccident'}
      },
      {
        path:'/vendorsetting',
        name: 'VendorSetting',
        component:()=>import('@/views/vendor/VendorSetting.vue'),
        meta:{title:'vendorsetting'}
      },
      { //简介页面
        path: '/introduce',
        name: 'Introduce',
        component: ()=>import('@/views/Introduce.vue'),
        meta:{title:'introduce'}
      },
      { //商品页面
        path: '/goodlist',
        name: 'GoodList',
        component: ()=>import('@/views/GoodList.vue'),
        meta:{title:'goodlist'}
      },
      { //axios测试页面
        path: '/testaxios',
        name: 'Testaxios',
        component: ()=>import('@/views/TestAxios.vue'),
        meta:{title:'testaxios'}
      },
      { //跨域请求测试
        path: '/crossdomain',
        name: 'CrossDomain',
        component: ()=>import('@/views/crossDomain/index.vue'),
        meta:{title:'crossdomain'}
      },
      { //获取环境变量页面
        path: '/env',
        name: 'Env',
        component: ()=>import('@/views/env/index.vue'),
        meta:{title:'env'}
      },
      { //文字识别
        path: '/characterRecognition',
        name: 'CharacterRecognition',
        component: ()=>import('@/views/characterRecognition/index3.vue'),
        meta:{title:'character recognition'}
      },
      { //图片上传
        path: '/imageUpload',
        name: 'ImageUpload',
        component: ()=>import('@/views/uploadImage/index6.vue'),
        meta:{title:'Image upload'}
      },
      { //分页
        path: '/pagination',
        name: 'Pagination',
        component: ()=>import('@/views/pagination/index.vue'),
        meta:{title:'分页'}
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
