from django.db import models


class Goods(models.Model):
    goods_title = models.CharField(max_length=20, blank=True, null=True)
    goods_price = models.CharField(max_length=20,blank=True,null=True)
    goods_image = models.FileField(blank=True, null=True, upload_to='goods', verbose_name='商品图片')
    goods_kind = models.CharField(max_length=20,blank=True, null=True)

    class Meta:  # 更改数据库表名称
        db_table = 'goods'  # 修改表名
        verbose_name = '商品类'    # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['goods_title']  # 排序字段

