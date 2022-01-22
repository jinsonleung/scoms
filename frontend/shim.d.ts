/*
 * @Author: Jinosn.Liang
 * @Date: 2022-01-12 20:46:17
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2022-01-22 20:11:50
 * @Description: 
 * @FilePath: /frontend/shim.d.ts
 */
/* eslint-disable */

// 声明文件，*.vue 后缀的文件交给 vue 模块来处理
declare module '*.vue' {
	import type { DefineComponent } from 'vue';
	const component: DefineComponent<{}, {}, any>;
	export default component;
}

// 声明qrcodejs2-fixes 交给vue模块处理,因为qrcodejs2-fixes没有ts版本
declare module "qrcodejs2-fixes" {
  export default require('qrcodejs2-fixes')
}

declare module "element-china-area-data" {
  export default require('element-china-area-data')
}

// 声明文件，定义全局变量。其它 app.config.globalProperties.xxx，使用 getCurrentInstance() 来获取
interface Window {
	nextLoading: boolean;
}
