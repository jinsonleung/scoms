from django.db import models
from django.conf import settings


class Customer(models.Model):
    company_account = models.CharField(max_length=16, unique=True, verbose_name='公司账号')
    company_name = models.CharField(max_length=128, blank=False, null=False, verbose_name='公司名称')
    company_abbreviation_name = models.CharField(max_length=64, null=True, verbose_name='公司简称')
    company_address = models.CharField(max_length=256, null=True, verbose_name='公司地址')
    city = models.CharField(max_length=32, null=True, verbose_name='所在城市')
    license_no = models.CharField(max_length=32,  null=True, verbose_name='营业执照号码')
    license_image = models.FileField(upload_to='customer', null=True, verbose_name='营业执照图片')
    registration_capital = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name='注册资金')    # 万元
    registration_date = models.DateTimeField(verbose_name='注册日期')
    registration_effect_start = models.DateTimeField(verbose_name='有效期开始日期')
    registration_effect_end = models.DateTimeField(verbose_name='有效期结束日期')
    industry = models.CharField(max_length=64, null=True, verbose_name='所在行业')
    contact_name = models.CharField(max_length=32, null=True, verbose_name='联系人姓名')
    contact_tel = models.CharField(max_length=128, null=True, verbose_name='联系人电话')
    contact_phone = models.CharField(max_length=64, null=True, verbose_name='联系人手机号码')
    is_available = models.BooleanField(default=False, verbose_name='是否启用')  # 默认为还没激活
    service_level = models.IntegerField(default=5, verbose_name='服务类别')  # 服务类别0-5，0为最高级别客户
    remark = models.TextField(max_length=1024, null=True, verbose_name='备注')
    is_delete = models.BooleanField(default=False, verbose_name='删除标志')  # 默认为还没删除
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='创建记录日期')   # 记录第一次创建时间，以后不会更新
    create_user = models.CharField(max_length=32, verbose_name='创建人')
    update_datetime = models.DateTimeField(auto_now=True, verbose_name='更新记录日期')   # 每次更新记录时就更新当前时间
    update_user = models.CharField(max_length=32, verbose_name='更新人')

    class Meta:  # 更改数据库表名称
        db_table = 'customer'  # 修改表名
        verbose_name = '客户类'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['company_account']  # 排序字段

    def __str__(self):
        return self.company_name