/*
 * @Author: Jinosn.Liang
 * @Date: 2022-01-07 11:33:08
 * @LastEditors: Jinson.Liang
 * @LastEditTime: 2022-01-08 09:46:49
 * @Description: 
 * @FilePath: /frontend/vite.config.ts
 */
import vue from '@vitejs/plugin-vue'
import {resolve} from 'path'
import type {UserConfig} from 'vite'
import {defineConfig} from "vite";
import {loadEnv} from './src/utils/viteBuild'

/**
 * 获取要目录
 * @param dir 目录名称
 * @returns 完整目录
 */
const pathResolve = (dir: string): any => {
    return resolve(__dirname, '.', dir)
}

// 别名数组对象
const alias: Record<string, string> = {
    // src目录别名
    '@': pathResolve('src'),
    // 国际货目录别名
    'vue-i18n': 'vue-i18n/dist/vue-i18n.cjs/js'
}

// 导入环境变量
const {VITE_PORT, VITE_OPEN, VITE_PUBLIC_PATH} = loadEnv();

const viteConfig: UserConfig = {
    plugins: [vue()],
    root: process.cwd(),
    resolve: {alias},
    server: {
        host: '0.0.0.0',
        port: VITE_PORT,
        open: VITE_OPEN,
        proxy: {
            /*
             将"/api/....“ 开头的请求地址进行代理
             如实际请求地址为https://imissu.herokuapp.com/api/v1/auth/register，参数为{"name":"aaa","email":"138923@qq.com","password":"232323","password2":"232323","role":"user"}
             则当系统使用http://localhost:3000/api/v1/auth/register，发起请求时，将/api更头的请求地址将本机地址使用target中的值进行替换，
             发起请求时使用"http.post('api/v1/auth/register', params).then((res: any) => {...}"即可
            */
            '/api': { //正确
                target: 'https://imissu.herokuapp.com',    //相当于/api = https://imissu.herokuapp.com
                changeOrigin: true,
                // rewrite: (path) => path.replace(/^\/api/, '')
            },
            '/books': { //正确
                target: 'http://127.0.0.1:8010',
                changeOrigin: true,
                //rewrite: (path) => path.replace(/^\/cc/, '')
            },
            // '/post': { // 前端URL=/post/
            //     target: 'https://jsonplaceholder.typicode.com',
            //     changeOrigin: true,
            //     //rewrite: (path) => path.replace(/^\/cc/, '')
            // },
            '/cc': { //
                target: 'http://tcc.taobao.com',
                changeOrigin: true,
                //rewrite: (path) => path.replace(/^\/cc/, '')
            },
            '/abc': { //
                target: 'http://suggest.taobao.com',
                changeOrigin: true,
                rewrite: (path) => path.replace(/^\/abc/, '')
            },
            '/ec': {    //正确
                target: 'https://e.qq.com', // 后端实际地址
                changeOrigin: true,
                // rewrite: path => path.replace(/^\/apiBase/, '')
            },
            '/ocr': {    // 正确
                target: 'http://127.0.0.1:8010', // 后端实际地址为http://127.0.0.1:8000/ocr/accurateocr，前端url为ocr/accurateocr
                changeOrigin: true,
                // rewrite: path => path.replace(/^\/apiBase/, '')
            },
            '/goods': {    // 正确
                target: 'http://127.0.0.1:8010', // 后端实际地址为http://127.0.0.1:8000/ocr/accurateocr，前端url为goods/accurateocr
                changeOrigin: true,
                // rewrite: path => path.replace(/^\/apiBase/, '')
            },
            '/customer': {    // 正确
                target: 'http://127.0.0.1:8000', // 后端实际地址为http://127.0.0.1:8000/ocr/accurateocr，前端url为goods/accurateocr
                changeOrigin: true,
                // rewrite: path => path.replace(/^\/apiBase/, '')
            }
        }
    },
    define: {
        'process.env': {},
        // __VUE_I18N_LEGACY_API__: JSON.stringify(false),
        // __VUE_I18N_FULL_INSTALL__: JSON.stringify(false),
        // __INTLIFY_PROD_DEVTOOLS__: JSON.stringify(false),
    },
}

export default viteConfig;

