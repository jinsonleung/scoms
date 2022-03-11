//全局注册自定义指令，用于判断当前图片是否能够加载成功，可以加载成功则赋值为img的src属性，否则使用默认图片
//参考：https://www.jianshu.com/p/394c487d81d7

/**
 * 判断图片地址是否存在，若存则显示，若不存在则显示默认地址的图片
 * default-image：为<img/>默认图片地址，如<img default-image="./assets/default.png"/>
 * 页面:
 * 1）main.ts中挂载
 *   import realImage from "/@/utils/directives/imageIsExist"
 *   app.use(realImage)
 * 2）页面：<image v-realimage="需要显示图片url", default-image="默认图片url" />
 * @param app:
 */
const realImage = (app: any) => {
    app.directive('realimage', async function (el: any, binding: any) {//指令名称为：v-realimage
        let imgURL = binding.value;//获取图片地址
        let defaultURL = el.getAttribute('default-image');//获取默认图片地址
        if (imgURL) {
            let exist = await imageIsExist(imgURL);
            if (exist) {
                el.setAttribute('src', imgURL);
            } else {
                if (defaultURL) {
                    el.setAttribute('src', defaultURL);
                }
            }
        }
    })
};


/**
 * 检测图片是否存在
 * @param url: 图片url
 */
let imageIsExist = function(url:any) {
    return new Promise((resolve) => {
        let img = new Image();
        img.onload = function () {
            if (this.complete == true){
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