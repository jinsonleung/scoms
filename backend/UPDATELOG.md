# <a href="">SCOMS 后台更新日志</a>
🔥 `SCOMS` 基于 python+django+mysql等后台系统

### 前端要求
- 🎉 新增 提供的日期格式为 YYYY-MM-DD HH:MM:SS


### 后端返回编码
- 4000：记录不存在
- 4001：记录已存在


### 常用方法
`2021.11.08`
- 🎉 生成requirements.txt  
`pip3 freeze > requirements.txt`
- 🎉 安装依赖环境   
`pip3 install -r requirements.txt`


### 版本：1.0.0
`2021.11.08`
- 🎉 新增 建立SCOMS后台框架

### 版本：1.0.1
`2022.01.08`

`2022.01.24`
- 🐞 修复 ‘cryptography‘ package is required for sha256_password or caching_sha2_password auth methods 解决方案   
```MySQL8.0之后身份验证插件导致的，取消MySql自动登录密码输入即可或先联系Mysql```

`2022.01.25`
- 🎯 学习：这个后端Django项目不错，“基于 django 3.X 的 RESTfulAPI 风格的项目模板，用于快速构建高性能的服务端” https://gitee.com/aeasringnar/django-RESTfulAPI 

`2022.01.26`
- 🎯 优化：添加apps目录，将所有app放在此目录下集中管理
- 🐞 Bug：common.model.BaseModel被继承后字段放在数据库表格前，**需要解决此问题**
- 🐞 Bug：保存字典至model还没处理完成，或参考：https://www.jb51.net/article/163765.htm


图标
- 🎯 优化 
- 🎯 优化 
- 🎉 新增 
- 🐞 修复 