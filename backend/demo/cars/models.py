from django.db import models

"""
外键位置配置
1）一对多：ForeignKey必须放在多的一方，书与出版社，外键应该放在书表
2）多对多：ManyToManyField放在任何一方都可以，因为会创建关系表，在关系表中用两个外键分别关联两个表
3）一对一：OneToOneField放在依赖的表，作者与作者详情，放在详情表，OneToOneField会被转换为 外键 + 唯一约束
"""


# 抽出来的基类
class BaseModel(models.Model):
    name = models.CharField(max_length=64, verbose_name='名称')
    is_delete = models.BooleanField(default=0, verbose_name='删除标志')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    class Meta:
        abstract = True     # 抽象类，不产生实际数据库表


class Car(BaseModel):
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='价格')
    brand = models.ForeignKey(to='Brand', related_name='Cars', db_constraint=False, on_delete=models.DO_NOTHING, verbose_name='品牌')
    sponsors = models.ManyToManyField(to="Sponsor", related_name="Cars", db_constraint=False, verbose_name='赞助商')

    class Meta:
        db_table = 'demo_car'   # 数据库表名
        verbose_name_plural = '汽车表'

    def __str__(self):
        return self.name

    def brand_(self):
        """自定义方法，返回品牌名称"""
        return self.brand.name

    # 多对多跨表查询
    def sponsors_(self):
        temp_sponsor_list = []  # 赞助商名称及电话列表
        for sponsor in self.sponsors.all():
            sponsor_dic = {"name": sponsor.name}
            try:
                sponsor_dic['电话'] = sponsor.detail.phone
            except:
                sponsor_dic['电话'] = ''
            temp_sponsor_list.append(sponsor_dic)
        return temp_sponsor_list


class Brand(BaseModel):
    class Meta:
        db_table = 'demo_brand'     # 数据库表名
        verbose_name_plural = '品牌表'

    def __str__(self):
        return self.name

    # 一对多跨表查询
    def car_list(self):
        temp_car_list = []  # 汽车名称列表
        for car_obj in self.Cars.all():
            car_dic = {
                "name": car_obj.name
            }
            try:
                car_dic['price'] = car_obj.price
            except:
                car_dic['price'] = ''
            temp_car_list.append(car_dic)
        return temp_car_list


class Sponsor(BaseModel):
    class Meta:
        db_table = 'demo_sponsor'   # 数据库表名
        verbose_name_plural = '赞助商表'

    def __str__(self):
        return self.name


class SponsorDetail(models.Model):
    class Meta:
        db_table = 'demo_sponsor_detail'
        verbose_name_plural = '赞助商详情表'

    phone = models.CharField(max_length=11)
    is_delete = models.BooleanField(default=1)
    updated_time = models.DateTimeField(auto_now=True)
    sponsor = models.OneToOneField(to="Sponsor", related_name="detail", on_delete=models.DO_NOTHING, db_constraint=False)