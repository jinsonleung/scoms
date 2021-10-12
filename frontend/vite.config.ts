import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import {resolve} from "path";

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [vue()],
    resolve: {
        alias: {  //映射别名
            '@': resolve(__dirname, 'src'), //@替代src目录，使用方法是 ‘@/views/layout/index.vue’，需要在tsconfig.ts中配置baseUrl和paths两个映射别名才能生效
        }
    },
    define: {
        'process.env': {}
    },
    server: {
        proxy: {
            '/books': {
                target: 'http://127.0.0.1:8000', //相当于http://127.0.0.1:8000/books
                //target: '',
                changeOrigin: true,
                rewrite: path => path.replace(/^\/books/, '')
            },
        }
    }
})


// 2. ===============================================================
// import vue from '@vitejs/plugin-vue'
// import {resolve} from "path";
// const path = require('path')
// // vite.config.js # or vite.config.ts
// // https://vitejs.dev/config/
// console.log(path.resolve(__dirname, './src'))
// module.exports = {
//   plugins: [vue()],
//   resolve: {
//     alias: {  //映射别名
//         '@': resolve(__dirname, './src'), //@替代src目录，使用方法是 ‘@/views/layout/index.vue’
//     }
//   },
//   hostname: '127.0.0.1',
//   port: 3000,
//   // 是否自动在浏览器打开
//   open: true,
//   // 是否开启 https
//   https: false,
//   // 服务端渲染
//   ssr: false,
//   /**
//    * 在生产中服务时的基本公共路径。
//    * @default '/'
//    */
//   base: './',
//   /**
//    * 与“根”相关的目录，构建输出将放在其中。如果目录存在，它将在构建之前被删除。
//    * @default 'dist'
//    */
//   outDir: 'dist',
//   // 反向代理，此处应该特别注意，网上很多教程是直接设置proxy，并没有向官网那样添加 server，可能会导致失败，vite官网：https://vitejs.dev/guide/features.html#async-chunk-loading-optimization
//   server:{
//     proxy: {
//       '/api': {
//         // target: 'https://api.pingping6.com/tools/baidutop/',
//         target: 'http://127.0.0.1:8000/books/',
//         changeOrigin: true,
//         rewrite: path => path.replace(/^\/api/, '')
//       }
//     }
//   }
// }