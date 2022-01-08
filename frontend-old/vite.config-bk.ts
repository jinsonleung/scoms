import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import {resolve} from "path";

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [vue()],
    resolve: {
        alias: {  //映射别名
            '@': resolve(__dirname, 'src'), //@替代src目录，使用方法是 ‘@/views/layout/index1.vue’，需要在tsconfig.ts中配置baseUrl和paths两个映射别名才能生效
        }
    },
    define: {
        'process.env': {}
    },
    server: {
        host:"0.0.0.0",
        port: 8010,     // 配置端口号
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
    }
})
