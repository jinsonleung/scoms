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
- 🎉 任意目录创建应用 cd 目录, django-admin startapp 应用名


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
- 🐞 Bug：保存字典至model还没处理完成，存储日期为空时报错，或参考：https://www.jb51.net/article/163765.htm
- 🐞 修复：报错“django.core.exceptions.ValidationError: ['“”的值有一个错误的日期格式。它的格式应该是YYYY-MM-DD']”，将前端传过来的字典中日期字段移除，再保存即可

`2022.01.28`
- 🐞 Bug：修改时出现，django.db.utils.IntegrityError: (1048, "Column 'create_datetime' cannot be null")
- 🎉 学习：自动记录创建人和修改人，https://blog.csdn.net/zgj0607/article/details/119943187?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_paycolumn_v3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2.pc_relevant_paycolumn_v3&utm_relevant_index=5

`2022.02.04`
- 🐞 Bug：分页还没有返回总记录条数，02/04已解决
- 
`2022.02.05`
- 🐞 Bug：DELETE请求时产生再次讲请求，一次是OPTIONS，这种OPTIONS应拒绝，如何拒绝OPTIONS请求？
- 🐞 Bug：提交前端表单时，PUT提交到后台后，返回需要个别字段是必须的问题，如create_by字段

`2022.02.10`
- 🎯 学习 drf中get/post/delete/put/patch五大接口(mixin方式) https://www.cnblogs.com/asdaa/p/11695099.html 




图标
- 🎯 优化 
- 🎯 优化 
- 🎉 新增 
- 🐞 修复 