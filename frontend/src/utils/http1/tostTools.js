/*
 * @Author: JinsonLiang
 * @Date: 2021-08-12 09:58:41
 * @LastEditors: JinsonLiang
 * @LastEditTime: 2021-08-12 11:43:33
 * @Description: file content
 * @FilePath: \vue3-vite-ssis\src\utils\http\tostTools.js
 */
import log from "./utils.log";
// 从"elementUI"中导入弹出提示信息的所用组件;
import { Message, Loading } from "element-ui";

// 创建一个错误
function errorCreate(msg) {
  const error = new Error(msg);
  errorLog(error);
  // throw error
}

// 记录和显示错误
function errorLog(error) {
  // 打印到控制台
  if (process.env.NODE_ENV === "development") {
    log.danger(">>>>>> Error >>>>>>");
    console.log(error);
  }
  // 显示提示
  tip(error.message);
}

// 轻提示
const tip = (msg) => {
  if (!msg) return;
  return Message({
    message: msg,
    duration: 3000,
  });
};

// 加载中
function loading(msg) {
  return Loading.service({
    lock: true,
    text: "拼命加载中...",
    spinner: "el-icon-loading",
    background: "rgba(0, 0, 0, 0.7)",
  });
}

export { errorCreate, errorLog, tip, loading };
