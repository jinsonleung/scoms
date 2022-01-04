/*
 * @Author: JinsonLiang
 * @Date: 2021-07-05 09:33:33
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-21 16:01:18
 * @Description: file content
 * @FilePath: \vue3-vite-ssis\src\store\index.ts
 */
import {createStore, Store, useStore as baseUseStore } from "vuex"
import app from '@/store/modules/app'
import topTags from '@/store/modules/topTags'
import system from '@/store/modules/system'
import {forEach} from "wangeditor/dist/utils/util";
import {RootStateTypes} from "@/store/interface";
import {InjectionKey} from "vue";

// Create a new store instance.
// const store = createStore({
//
//     modules: {
//       // app,
//       // topTags,  //顶部菜单标签栏
//       system,
//     },
//     // 单独模块引入，每个模块都有单独的state，getters，actions， mutations
//     // state,  共同维护的一个状态，state里面可以是很多个全局状态
//     // getters, 获取数据并渲染
//     // actions, 数据的异步操作，操作复杂的逻辑。
//     // mutations 处理数据的唯一途径，state的改变或赋值只能在这里
//   })
//
//   export default store;


// const store:any = createStore({
//     modules: {
//       // app,
//       // topTags,  //顶部菜单标签栏
//       system,
//     },
//     // 单独模块引入，每个模块都有单独的state，getters，actions， mutations
//     // state,  共同维护的一个状态，state里面可以是很多个全局状态
//     // getters, 获取数据并渲染
//     // actions, 数据的异步操作，操作复杂的逻辑。
//     // mutations 处理数据的唯一途径，state的改变或赋值只能在这里
//   })
//
//   export default store;



// Vite 支持使用特殊的 import.meta.glob 函数从文件系统导入多个模块
// see https://cn.vitejs.dev/guide/features.html#glob-import
// 获取将modules目录下所有.ts文件名，如'./modules/userInfos.ts'
const modulesFiles = import.meta.glob('./modules/*.ts')
// 模块文件路径数组
const pathList: string [] = []
// 将modulesFiles对象中的文件路径存入pathList中
for (const path in modulesFiles) {
    pathList.push(path)
}

	console.log('==pathList==', pathList)


// 获取模板,如'{state:{},mutations:{},action:s{}},...'
const modules = pathList.reduce((modules: { [x: string]: any }, modulePath: string) => {
	const moduleName = modulePath.replace(/^\.\/modules\/(.*)\.\w+$/, '$1');
	console.log('==moduleName==', moduleName)
	const value = modulesFiles[modulePath];
    console.log('==value==', value)
	modules[moduleName] = value.default;
	// modules[moduleName] = value;
	return modules;
}, {});

console.log('==modules==', modules)

export const store = createStore<RootStateTypes>({ modules })

export const key: InjectionKey<Store<RootStateTypes>> = Symbol();
export function useStore() { return baseUseStore(key)}

