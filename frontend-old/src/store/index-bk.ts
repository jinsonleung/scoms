/*
 * @Author: JinsonLiang
 * @Date: 2021-07-05 09:33:33
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2021-08-21 16:01:18
 * @Description: file content
 * @FilePath: \vue3-vite-ssis\src\store\index.ts
 */
import {createStore, Store, useStore as baseUseStore } from "vuex"
import {RootStateTypes} from "@/store/interface";
import {InjectionKey} from "vue";

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
	// modules[moduleName] = value.default;
	modules[moduleName] = value;
	return modules;
}, {});

console.log('==modules==', modules)

export const store = createStore<RootStateTypes>({ modules })

export const key: InjectionKey<Store<RootStateTypes>> = Symbol();
export function useStore() { return baseUseStore(key)}

