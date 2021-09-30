/*
 * @Author: JinsonLiang
 * @Date: 2021-08-14 17:33:17
 * @LastEditors: JinsonLiang
 * @LastEditTime: 2021-08-14 17:50:39
 * @Description: 获取环境变量函数
 * @FilePath: \vue3-vite-ssis\src\utils\env.ts
 */

import { IEnv }  from '@/type/store/interface'  //引入环境变量接口


/**
 * 获取环境变量
 *
 * @export 环境变量对象
 * @return {*}  {IEnv}
 */
export function envs(): IEnv {
    let env: IEnv = {
        MODE: import.meta.env.MODE, //import.meta.env.MODE,
        PORT: 3305,
        // @ts-ignore
        PORT_STRING: import.meta.env.VITE_PORT || '3305',
        // @ts-ignore
        APP_BASE_API: import.meta.env.VITE_APP_BASE_API || '',
        // @ts-ignore
        APP_BASE_URL: import.meta.env.VITE_APP_BASE_URL || '',
    }
    env.PORT = parseInt(env.PORT_STRING)
    return env
}

