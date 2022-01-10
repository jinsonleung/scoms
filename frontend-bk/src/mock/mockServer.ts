/*
 * @Author: Jinson.Liang
 * @Date: 2021-08-18 09:37:20

 * @Description:
 * @FilePath: \vue3-vite-ssis\src\mock\mockServer.ts
 */
import Mock, { mock } from "mockjs"
import { loginMock, checkLogin} from "./loginMock"
import { getListData } from './goodList'
import { getAllCustomer, getPageCustomer } from "./customerList"



/*
1）mockjs不用设置vite.config.ts中的路跨域代理
2）在页面中import '@/mock/mockServer'即可使用
 */

Mock.mock("/user/info", loginMock) //用户登录mock，正确
Mock.mock("http://localhost:3000/user/info", loginMock) //用户登录mock，错误（不用加前缀）
Mock.mock("/adminUser/login", "get",loginMock) //用户登录mock，正确

Mock.mock("/adminUser/checkLogin", 'post', checkLogin) //用户登录检查，正确

//Mock.mock(RegExp("getList" + ".*"),'get', getListData)

Mock.mock('/getlistdata', getListData)  //獲取商品列表
//Mock.mock('/getGoodslist','get', getGoodsList(params: listQuery))  //獲取商品列表

// 获取客户列表，正确
Mock.mock('/mockcustomer/getall', 'get', getAllCustomer)  //正确，获取Mock的客户列表，页面访问http.get('/mockcustomer/getall').then

// 获取分页客户列表，带参访问，必须有正则表达式才能切尔西到/mockcustomer/getpage?limit=10&office=0这种请求地址
// Mock.mock('/mockcustomer/getpage', 'get', getPageCustomer)  //，获取Mock的客户列表，页面访问http.get('/mockcustomer/getall').then
Mock.mock(RegExp('/mockcustomer/getpage'+'.*'), 'get', getPageCustomer)  //正确，获取Mock的客户列表，页面访问http.get('/mockcustomer/getall').then


