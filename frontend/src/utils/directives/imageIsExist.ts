//全局注册自定义指令，用于判断当前图片是否能够加载成功，可以加载成功则赋值为img的src属性，否则使用默认图片
//参考：https://www.jianshu.com/p/394c487d81d7

// import Vue from 'vue';
// const app = Vue.createApp({});

const realImage = (app: any) => {
    app.directive('realimage', async function (el, binding) {//指令名称为：real-img
        let imgURL = binding.value;//获取图片地址
        if (imgURL) {
            let exist = await imageIsExist(imgURL);
            if (exist) {
                el.setAttribute('src', imgURL);
            }
        }
    })
}

/**
 * 检测图片是否存在
 * @param url
 */
let imageIsExist = function(url) {
    return new Promise((resolve) => {
        var img = new Image();
        img.onload = function () {
            if (this.complete){
                resolve(true);
                img = null;
            }
        }
        img.onerror = function () {
            resolve(false);
            img = null;
        }
        img.src = url;
    })
}

export default realImage