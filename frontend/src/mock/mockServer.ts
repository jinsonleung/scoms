/*
 * @Author: Jinson.Liang
 * @Date: 2021-08-18 09:37:20

 * @Description:
 * @FilePath: \vue3-vite-ssis\src\mock\mockServer.ts
 */
import Mock, { mock } from "mockjs"
import { loginMock, checkLogin} from "./loginMock"
import { getListData } from './goodList'





Mock.mock("/user/info", loginMock) //用户登录mock，正确
Mock.mock("http://localhost:3000/user/info", loginMock) //用户登录mock，错误（不用加前缀）
Mock.mock("/adminUser/login", "get",loginMock) //用户登录mock，正确

Mock.mock("/adminUser/checkLogin", 'post', checkLogin) //用户登录检查，正确

//Mock.mock(RegExp("getList" + ".*"),'get', getListData)

Mock.mock('/getlistdata', getListData)  //獲取商品列表
//Mock.mock('/getGoodslist','get', getGoodsList(params: listQuery))  //獲取商品列表


