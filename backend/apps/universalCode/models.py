from django.db import models
from apps.public.models import BaseModel
from apps.public.managers import CommonManager


class Continent(BaseModel):
    """
    全球洲表，继承抽象基类BaseModel
    """
    eng_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='国家英文全称')
    chn_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='国家中文全称')
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name='描述')

    objects = models.Manager()   # 默认模型管理器

    class Meta:
        db_table = 'continent'  # 数据库实际表名
        verbose_name = '全球各洲表'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['eng_name']  # 排序字段

    def __str__(self):
        return self.eng_name


class Country(BaseModel):
    """
    全球国家两表，继承抽象基类BaseModel
    """
    iso2_code = models.CharField(max_length=16, blank=False, null=False, unique=True, verbose_name='国家两字码')
    iso3_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='国家三字码')
    eng_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='国家英文')
    full_eng_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='国家英文全称')
    chn_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='国家中文')
    full_chn_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='国家中文全称')
    language = models.CharField(max_length=64, blank=True, null=True, verbose_name='所用语言')
    phone_code = models.CharField(max_length=64, blank=True, null=True, verbose_name='电话区号')
    capital = models.CharField(max_length=64, blank=True, null=True, verbose_name='首都')
    currency = models.CharField(max_length=64, blank=True, null=True, verbose_name='货币')
    native = models.CharField(max_length=128, blank=True, null=True, verbose_name='种族')
    emoji = models.CharField(max_length=64, blank=True, null=True, verbose_name='emoji')
    emojiU = models.CharField(max_length=128, blank=True, null=True, verbose_name='emoji图标')
    wiki_data_id = models.CharField(max_length=64, blank=True, null=True, verbose_name='维基数据代码')
    continent = models.ForeignKey(Continent, blank=True, null=True, on_delete=models.CASCADE, verbose_name='所在洲id(外键)')
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name='描述')

    objects = models.Manager()   # 默认模型管理器
    custom = CommonManager()

    class Meta:
        db_table = 'country'  # 数据库实际表名
        verbose_name = '全球国家两字码表'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['iso2_code']  # 排序字段

    def __str__(self):
        return self.iso2_code


class State(BaseModel):
    """
    全球省份表
    """
    iso2_code = models.CharField(max_length=16, blank=False, null=False, verbose_name='省两字码(可重复)')
    eng_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='省英文全称')
    chn_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='省中文全称')
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.CASCADE, verbose_name='所在国家id(外键)')
    country_iso2_code = models.CharField(max_length=32, blank=True, null=True, verbose_name='国家代码')
    fips_code = models.CharField(max_length=64, blank=True, null=True, verbose_name='fips代码')
    wiki_data_id = models.CharField(max_length=64, blank=True, null=True, verbose_name='维基数据代码')
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name='描述')

    objects = models.Manager()   # 默认模型管理器

    class Meta:
        db_table = 'state'  # 数据库实际表名
        verbose_name = '全球各洲表'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['iso2_code']  # 排序字段

    def __str__(self):
        return self.iso2_code


class City(BaseModel):
    """
    全球城市三字码表，继承抽象基类BaseModel
    country：外键，关联country
    国家：城市=1：N
    """
    iso3_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='城市三字码(先设置为空，以后再补)')
    eng_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='城市英文全称')
    chn_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='城市中文全称')
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.CASCADE, verbose_name='所在国家id')
    country_iso2_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='所在国家二字码')
    state = models.ForeignKey(State, blank=True, null=True, on_delete=models.CASCADE, verbose_name='所在省份id')
    state_iso2_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='所在省份二字码')
    latitude = models.CharField(max_length=64, blank=True, null=True, verbose_name='纬度')
    longitude = models.CharField(max_length=64, blank=True, null=True, verbose_name='经度')
    wiki_data_id = models.CharField(max_length=64, blank=True, null=True, verbose_name='维基数据代码')
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name='描述')

    objects = models.Manager()   # 默认模型管理器
    custom = CommonManager()

    class Meta:
        db_table = 'city'  # 数据库实际表名
        verbose_name = '全球城市三字码表'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['iso3_code']  # 排序字段

    def __str__(self):
        return self.iso3_code


class Airport(BaseModel):
    """
    全球机场三字码表，继承抽象基类BaseModel
    country_code外键关联全球国家两字码表，国家：机场=1：N，城市：机场=1：N
    city_code没有关联城市全球城市三字码表（原因是城市三字码表还没有包含所有机场所在城市）
    """
    iata_code = models.CharField(max_length=16, blank=False, null=False, unique=True, verbose_name='IATA机场代码')
    icao_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='ICAO机场代码')
    eng_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='机场英文名称')
    chn_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='机场中文名称')
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.CASCADE, verbose_name='所在国家')
    country_iso2_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='国家二字码')
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.CASCADE, verbose_name='所在城市id')
    city_iso3_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='城市三字码')
    city_eng_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='城市英文名称')
    city_chn_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='城市中文名称')
    elevation = models.CharField(max_length=64, blank=True, null=True, verbose_name='海拨高度')
    latitude = models.CharField(max_length=64, blank=True, null=True, verbose_name='纬度')
    longitude = models.CharField(max_length=64, blank=True, null=True, verbose_name='经度')
    time_zone = models.CharField(max_length=64, blank=True, null=True, verbose_name='时区')
    utc = models.CharField(max_length=16, blank=True, null=True, verbose_name='UTC时差')
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name='描述')

    objects = models.Manager()   # 默认模型管理器
    custom = CommonManager()    # 自定义模型管理器

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
    eng_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='机场英文名称')
    chn_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='机场中文名称')
    call_sign = models.CharField(max_length=64, blank=True, null=True, verbose_name='机场英文名称')
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.CASCADE, verbose_name='所在国家id(外键)')
    country_iso2_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='国家二字码')
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.CASCADE, verbose_name='所在城市id(外键)')
    city_iso3_code = models.CharField(max_length=16, blank=True, null=True, verbose_name='城市三字码')
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
