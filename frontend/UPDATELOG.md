# <a href="">SCOMS 更新日志</a>
🔥 `SCOMS` 基于 vue3.x+Typescript+vite+Element plus 等，适配手机、平板、pc 的后台管理板系统

### 版本：1.0.0
`2022.01.08`
- 🎉 新增 使用vue3.x+Typescript+vite+Element plus

### 版本：1.0.1
`2022.01.08`
- 🐞 修复 src/views/login/component/scan.vue qrcodejs2-fixes 引入时报错
   - 原因：插件没有ts版本的，在shim.d.ts中声明使用js包即可
    ```angular2html
    declare module "qrcodejs2-fixes" {
      export default require('qrcodejs2-fixes')
    }
    ```
`2022.01.11`
- 🎯 优化 添加了Logo

`2022.01.12`
- 🎯 优化 更新了菜单栏背景色
- 🐞 修复 注掉app.vue中的第3方baidu js库

`2022.01.19`
- 🐞 enterprise/addNewEnterprise.vue前端的日期格式后端不接受


图标
- 🎯 优化 
- 🎯 优化 
- 🎉 新增 
- 🐞 修复 

