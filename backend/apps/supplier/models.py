from django.db import models
from apps.public.models import BaseModel
from apps.public.managers import CommonManager


class Supplier(BaseModel):
    """
    供应商表，继承抽象基类BaseModel
    """
    account = models.CharField(max_length=16, blank=False, null=False, unique=True, verbose_name='账号')
    abbreviation_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='简称')
    full_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='全称')
    architecture = models.CharField(max_length=64, blank=True, null=True, verbose_name='体系结构（总部/分公司/子公司）')
    unified_social_credit_code = models.CharField(max_length=32,  blank=True, null=True, verbose_name='统一社会信用代码')
    registered_capital = models.CharField(max_length=32, blank=True, null=True, verbose_name='注册资本')
    registered_address = models.CharField(max_length=32, blank=True, null=True, verbose_name='注册地址')
    established_date = models.DateField(blank=True, null=True, verbose_name='成立日期')
    effective_start_date = models.DateField(blank=True, null=True, verbose_name='营业期限(起)')
    effective_end_date = models.DateField(blank=True, null=True, verbose_name='营业期限(止)')
    office_address = models.CharField(max_length=128, blank=True, null=True, verbose_name='办公地址')
    business_scope = models.TextField(max_length=128, blank=True, null=True, verbose_name='经营范围')
    country = models.CharField(max_length=64, blank=True, null=True, verbose_name='所在国家')
    province = models.CharField(max_length=64, blank=True, null=True, verbose_name='所在省/洲')
    city = models.CharField(max_length=64, blank=True, null=True, verbose_name='所在城市')
    district = models.CharField(max_length=64, blank=True, null=True, verbose_name='所在区/县')
    industry = models.CharField(max_length=32, blank=True, null=True, verbose_name='所在行业')
    website = models.CharField(max_length=64, blank=True, null=True, verbose_name='企业网站')
    legal_person_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='法人姓名')
    legal_person_phone = models.CharField(max_length=64, blank=True, null=True, verbose_name='法人电话')
    legal_person_email = models.CharField(max_length=64, blank=True, null=True, verbose_name='法人邮箱')
    banking_account_info = models.TextField(max_length=256, blank=True, null=True, verbose_name='银行对公账户信息')
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name='描述')
    is_available = models.BooleanField(default=False, verbose_name='是否启用')  # 默认为还没激活

    objects = models.Manager()   # 默认模型管理器
    custom = CommonManager()    # 自定义管理器

    class Meta:
        db_table = 'supplier'  # 数据库实际表名
        verbose_name = '供应商表'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['account']  # 排序字段

    def __str__(self):
        return '%s,%s' (self.account, self.full_name)


class SupplierContact(models.Model):
    """
    供应商联系人表
    """
    CLASSIFICATIONS = (
        ('GM', '总经办'),
        ('LO', '对接人'),  # liaison officer
        ('FI', '财务'),
        ('SA', '销售'),
        ('OP', '运营'),
        ('LG', '法务'),
        ('PU', '采购'),
        ('IT', 'IT'),
        ('HR', 'HR'),
    )
    classification = models.CharField(max_length=32, blank=True, null=True, choices=CLASSIFICATIONS,
                                      verbose_name='岗位类别(如财务/销售/..)')
    name = models.CharField(max_length=32, blank=True, null=True, verbose_name='联系人姓名')
    tel = models.CharField(max_length=64, blank=True, null=True, verbose_name='联系人电话')
    phone = models.CharField(max_length=64, blank=True, null=True, verbose_name='联系人手机')
    email = models.CharField(max_length=64, blank=True, null=True, verbose_name='联系人邮箱')
    remark = models.TextField(max_length=256, blank=True, null=True, verbose_name='备注')
    supplier = models.ForeignKey(Supplier, blank=True, null=True, on_delete=models.CASCADE, verbose_name='供应商id(外键)')

    objects = models.Manager()  # 默认模型管理器

    class Meta:
        db_table = 'supplier_contact'  # 数据库实际表名
        verbose_name = '供应商联系人表'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['classification']  # 排序字段

    def __str__(self):
        return '%s,%s' (self.classification, self.name)
