//全局注册自定义指令，用于判断当前图片是否能够加载成功，可以加载成功则赋值为img的src属性，否则使用默认图片
//参考：https://www.jianshu.com/p/394c487d81d7

// import Vue from 'vue';
// const app = Vue.createApp({});

import {consoleLog} from "echarts/types/src/util/log";

const realImage = (app: any, options: any) => {
    app.directive('realimage', async function (el: any, binding: any) {//指令名称为：v-realimage
        let imgURL = binding.value;//获取图片地址
        if (imgURL) {
            let exist = await imageIsExist(imgURL);
            if (exist) {
                el.setAttribute('src', imgURL);
            }
        }
    })
};


/**
 * 检测图片是否存在
 * @param url
 */
let imageIsExist = function(url:any) {
    return new Promise((resolve) => {
        let img = new Image();
        console.log('==img==', img)
        img.onload = function () {
            if (this.complete == true){
                resolve(true);
                img = null;
            }
            console.log('==img.onload==')
        }
        img.onerror = function () {
            resolve(false);
            img = null;
            console.log('==img.onerror==')
        }
        img.src = url;
    })
}

export default realImage