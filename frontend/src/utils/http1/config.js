/*
 * @Author: JinsonLiang
 * @Date: 2021-08-12 09:58:41
 * @LastEditors: JinsonLiang
 * @LastEditTime: 2021-08-12 11:43:25
 * @Description: file content
 * @FilePath: \vue3-vite-ssis\src\utils\http\config.js
 */
let baseUrl = "http://localhost:8080/api"; // 这儿就是定义的公共请求接口地址

// 环境的切换
if (process.env.NODE_ENV === "development") {
  baseUrl = "http://localhost:8080/api"; // 开发环境ip地址
} else if (process.env.NODE_ENV === "debug") {
  baseUrl = "http://localhost:8080/api"; // 测试环境ip地址
} else if (process.env.NODE_ENV === "production") {
  baseUrl = "http://localhost:8080/api"; // 线上生产环境ip地址
}

export default {
  // 请求域名
  HTTP_REQUEST_URL: baseUrl,

  // Socket链接 暂不做配置，保留字段
  WSS_SERVER_URL: "",

  // 默认请求头信息
  HEADER: {
    "content-type": "application/json",
  },

  // Socket调试模式，暂不考虑
  SERVER_DEBUG: true,

  // websocket的心跳间隔，暂不考虑
  PINGINTERVAL: 3000,

  // 后台接收token信息的键（key）名
  TOKENNAME: "TOKEN",

  // 返回给后台token的格式，在这里跟后端约定传入的token格式。比如token需要 md5 加密传输 (token) => md5(token)，md5 需要安装依赖并引用
  TOKEN_FORMAT: (token) => token,

  // 用户信息缓存名称   开发者服务器平台返回的用户数据
  CACHE_USERINFO: "USERINFO",

  // token缓存名称，缓存到本地localStorage的键名
  CACHE_TOKEN: "TOKEN",

  // token过期事件，一般后台接口有token过期处理判断
  CACHE_EXPIRES_TIME: "EXPIRES_TIME",
};
