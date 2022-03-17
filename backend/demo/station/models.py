from django.db import models


# 图书类
class Station(models.Model):
    station_code = models.CharField(max_length=16, blank=False, null=False, unique=True)
    station_name = models.CharField(max_length=32, blank=False, null=False)
    station_address = models.CharField(max_length=100, blank=False, null=False)
    facility_code = models.CharField(max_length=16, blank=False, null=False)
    employees = models.CharField(max_length=16, blank=False, null=False)
    update_datetime = models.DateTimeField(auto_now=True)  # 在每次这个数据保存的时候，都使用当前的时间
    is_delete = models.BooleanField()
    create_datetime = models.DateTimeField(auto_now_add=True)  # 在每条数据第一次被添加进去的时候，使用当前的时间
    create_user = models.CharField(max_length=32, blank=False, null=False)

    class Meta:  # 更改数据库表名称
        db_table = 'station'  # 修改表名
        verbose_name = '场站类'    # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['station_code']     # 排序字段