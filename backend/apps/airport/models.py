from django.db import models
from rest_framework.fields import ListField
from apps.common.models import BaseModel
from apps.common.managers import CommonManager


class Airport(BaseModel):
    """全球机场三字码表，继承抽象基类BaseModel"""
    # id = models.SmallAutoField(primary_key=True, verbose_name='自增主键') # django会自动增加自增主键
    iata_code = models.CharField(max_length=16, blank=False, null=False, unique=True, verbose_name='IATA机场代码')
    icao_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='ICAO机场代码')
    airport_chn_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='机场中文名称')
    airport_eng_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='机场英文名称')
    country_code = models.CharField(max_length=32, blank=True, null=True, verbose_name='国家/地区代码')
    country_chn_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='国家/地区中文名称')
    country_eng_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='国家/地区英文名称')
    city_chn_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='城市中文名称')
    city_eng_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='城市英文名称')
    elevation = models.CharField(max_length=64, blank=True, null=True, verbose_name='海拨高度')
    longitude = models.CharField(max_length=64, blank=True, null=True, verbose_name='经度')
    latitude = models.CharField(max_length=64, blank=True, null=True, verbose_name='纬度')
    time_zone = models.CharField(max_length=64, blank=True, null=True, verbose_name='时区')
    utc = models.CharField(max_length=16, blank=True, null=True, verbose_name='UTC时差')
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name='描述')
    is_available = models.BooleanField(default=True, verbose_name='是否启用')  # 默认为可使用

    objects = models.Manager()   # 默认模型管理器
    custom = CommonManager()

    class Meta:
        db_table = 'airport'  # 数据库实际表名
        verbose_name = '全球机场三字码表'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['iata_code']  # 排序字段

    def __str__(self):
        return self.iata_code