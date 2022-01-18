from django.db import models
from django.conf import settings

# 企业信息表
class Enterprise(models.Model):
    id = models.SmallAutoField(primary_key=True, verbose_name='自增主键')
    enterprise_level = models.CharField(max_length=64, blank=True, null=True, verbose_name='上级企业')
    account = models.CharField(max_length=16, unique=True, verbose_name='企业账号')
    full_name = models.CharField(max_length=64, blank=False, null=False, verbose_name='企业名全称')
    abbreviation_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='企业名简称')
    enterprise_type = models.CharField(max_length=32, blank=False, null=False, verbose_name='企业类型')
    architecture = models.CharField(max_length=64, blank=False, null=False, verbose_name='体系结构（总部/分公司/子公司）')
    unified_social_credit_code = models.CharField(max_length=32,  null=True, verbose_name='统一社会信用代码')
    registered_capital = models.CharField(max_length=32, blank=True, null=True, verbose_name='注册资本')
    established_date = models.DateTimeField(blank=True, null=True, verbose_name='成立日期')
    effective_start_date = models.DateTimeField(blank=True, null=True, verbose_name='营业期限(起)')
    effective_end_date = models.DateTimeField(blank=True, null=True, verbose_name='营业期限(止)')
    address = models.CharField(max_length=128, null=True, verbose_name='公司地址')
    city = models.CharField(max_length=32, null=True, verbose_name='所在城市')
    industry = models.CharField(max_length=32, null=True, verbose_name='所在行业')
    website = models.CharField(max_length=64, blank=True, null=True, verbose_name='企业网站')
    legal_person_name = models.CharField(max_length=16, blank=True, null=True, verbose_name='企业法人姓名')
    legal_person_email = models.CharField(max_length=64, blank=True, null=True, verbose_name='企业法人邮箱')
    contact_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='联系人姓名')
    contact_tel = models.CharField(max_length=32, blank=True, null=True, verbose_name='联系人电话')
    contact_phone = models.CharField(max_length=32, blank=True, null=True, verbose_name='联系人手机号码')
    contact_email = models.CharField(max_length=64, blank=True, null=True, verbose_name='联系人邮箱')
    business_scope = models.TextField(max_length=256, blank=True, null=True, verbose_name='经营范围')
    remark = models.TextField(max_length=256, blank=True, null=True, verbose_name='备注')
    is_available = models.BooleanField(default=False, verbose_name='是否启用')  # 默认为还没激活
    is_delete = models.BooleanField(default=False, verbose_name='删除标志')  # 默认为还没删除
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='创建记录日期')   # 记录第一次创建时间，以后不会更新
    create_by = models.CharField(max_length=32, blank=False, null=False, verbose_name='创建人')
    update_datetime = models.DateTimeField(auto_now=True, verbose_name='更新记录日期')   # 每次更新记录时就更新当前时间
    update_by = models.CharField(max_length=32, blank=False, null=False, verbose_name='更新人')

    class Meta:  # 更改数据库表名称
        db_table = 'enterprise'  # 修改表名
        verbose_name = '企业信息表'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['account']  # 排序字段

    def __str__(self):
        return self.account
