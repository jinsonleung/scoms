## DRF序列化高级
### 自定义只读只写、序列化覆盖字段、二次封装Response、数据库查询优化(断关联)、十大接口、视图家族
ref:http://www.zyiz.net/tech/detail-109273.html#models.py

#### 1.功能：
此Demo演示一对一、一对多、多对多序列化及CRUD

#### 2.类关系：
brand（品牌）       1
car（汽车）         n           n
sponsor（赞助商）           1
sponsorDetail（赞助商详细）  1   n  

#### 3.外键位置：
1）一对多：ForeignKey必须放在多的一方，书与出版社，外键应该放在书表
2）多对多：ManyToManyField放在任何一方都可以，因为会创建关系表，在关系表中用两个外键分别关联两个表
3）一对一：OneToOneField放在依赖的表，作者与作者详情，放在详情表，OneToOneField会被转换为 外键 + 唯一约束


