from django.db import models
from apps.public.models import BaseModel
from apps.public.managers import CommonManager


class Country(BaseModel):
    """
    全球国家两字码表，继承抽象基类BaseModel
    code:主键
    """
    code = models.CharField(primary_key=True, max_length=16, blank=False, null=False, unique=True, verbose_name='国家两字码')
    chn_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='国家中文全称')
    eng_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='国家英文全称')
    continent = models.CharField(max_length=64, blank=True, null=True, verbose_name='所在洲')
    tel_zone = models.CharField(max_length=32, blank=True, null=True, verbose_name='电话区号')
    time_difference = models.CharField(max_length=32, blank=True, null=True, verbose_name='时差')
    national_flag_img = models.CharField(max_length=128, blank=True, null=True, verbose_name='国旗图片')
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name='描述')

    objects = models.Manager()   # 默认模型管理器
    custom = CommonManager()

    class Meta:
        db_table = 'country'  # 数据库实际表名
        verbose_name = '全球国家两字码表'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['code']  # 排序字段

    def __str__(self):
        return self.code


class City(BaseModel):
    """
    全球城市三字码表，继承抽象基类BaseModel
    city_code：主键；country_code：外键，关联country.country_code
    国家：城市=1：N
    """
    code = models.CharField(primary_key=True, max_length=16, blank=False, null=False, unique=True, verbose_name='城市三字码')
    country_code = models.ForeignKey(to='Country', to_field='code', blank=True, null=True, on_delete=models.CASCADE, verbose_name='国家两字码')
    eng_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='城市英文全称')
    chn_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='城市中文全称')
    time_zone = models.CharField(max_length=32, blank=True, null=True, verbose_name='时区')
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name='描述')

    objects = models.Manager()   # 默认模型管理器
    custom = CommonManager()

    class Meta:
        db_table = 'city'  # 数据库实际表名
        verbose_name = '全球城市三字码表'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['code']  # 排序字段

    def __str__(self):
        return self.code


class Airport(BaseModel):
    """
    全球机场三字码表，继承抽象基类BaseModel
    iata_code:主键
    country_code外键关联全球国家两字码表，国家：机场=1：N，城市：机场=1：N
    city_code没有关联城市全球城市三字码表（原因是城市三字码表还没有包含所有机场所在城市）
    """
    iata_code = models.CharField(primary_key=True, max_length=16, blank=False, null=False, unique=True, verbose_name='IATA机场代码')
    icao_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='ICAO机场代码')
    chn_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='机场中文名称')
    eng_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='机场英文名称')
    country_code = models.ForeignKey(to='Country', to_field='code', on_delete=models.CASCADE, blank=True, null=True, verbose_name='所在国家')
    city_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='城市三字码')
    city_chn_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='城市中文名称')
    city_eng_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='城市英文名称')
    elevation = models.CharField(max_length=64, blank=True, null=True, verbose_name='海拨高度')
    longitude = models.CharField(max_length=64, blank=True, null=True, verbose_name='经度')
    latitude = models.CharField(max_length=64, blank=True, null=True, verbose_name='纬度')
    time_zone = models.CharField(max_length=64, blank=True, null=True, verbose_name='时区')
    utc = models.CharField(max_length=16, blank=True, null=True, verbose_name='UTC时差')
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name='描述')

    objects = models.Manager()   # 默认模型管理器
    custom = CommonManager()

    class Meta:
        db_table = 'airport'  # 数据库实际表名
        verbose_name = '全球机场三字码表'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['iata_code']  # 排序字段

    def __str__(self):
        return self.iata_code


class Airline(BaseModel):
    """
    全球航空公司二字码表，继承抽象基类BaseModel
    主键：id(自动生成，自增主键)
    country_code外键关联全球国家两字码表，国家：机场=1：N，城市：机场=1：N
    city_code没有关联城市全球城市三字码表（原因是城市三字码表还没有包含所有机场所在城市）
    """
    iata_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='IATA机场代码')
    icao_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='ICAO机场代码')
    accounting_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='ICAO机场代码')
    airline_prefix_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='ICAO机场代码')
    chn_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='机场中文名称')
    eng_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='机场英文名称')
    call_sign = models.CharField(max_length=64, blank=True, null=True, verbose_name='机场英文名称')
    country_code = models.ForeignKey(to='Country', to_field='code', on_delete=models.CASCADE, max_length=16, blank=True, null=True, verbose_name='所在国家')
    city_code = models.ForeignKey(to='City', to_field='code', on_delete=models.CASCADE, max_length=16, blank=True, null=True, verbose_name='城市三字码')
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name='描述')

    objects = models.Manager()   # 默认模型管理器
    custom = CommonManager()

    class Meta:
        db_table = 'airline'  # 数据库实际表名
        verbose_name = '全球航空公司二字码表'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['iata_code']  # 排序字段

    def __str__(self):
        return self.iata_code