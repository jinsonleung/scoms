from django.db import models
from apps.common.models import BaseModel


class EnterpriseManager(models.Manager):
    # 自定义模型管理器，继承了models.Manager并重父类的方法get_queryset()
    def get_queryset(self):
        # 过滤并保留is_delete标志为False的记录
        return super(EnterpriseManager, self).get_queryset().filter(is_delete=False)

    # 在这里定义管理器的其他方法,如
    # def create(self, title):
    #     # 创建
    #     enterprise = self.create(title=title)
    #     # do something with the book
    #     enterprise.save()
    #     return enterprise


class Enterprise(BaseModel):
    # 企业信息表，继承抽象基类BaseModel
    id = models.SmallAutoField(primary_key=True, verbose_name='自增主键')
    superior_level = models.CharField(max_length=64, blank=True, null=True, verbose_name='上级企业')
    account = models.CharField(max_length=16, unique=True, verbose_name='企业账号')
    full_name = models.CharField(max_length=64, blank=False, null=False, verbose_name='企业名全称')
    abbreviation_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='企业名简称')
    enterprise_type = models.CharField(max_length=32, blank=False, null=False, verbose_name='企业类型')
    architecture = models.CharField(max_length=64, blank=False, null=False, verbose_name='体系结构（总部/分公司/子公司）')
    unified_social_credit_code = models.CharField(max_length=32,  null=True, verbose_name='统一社会信用代码')
    registered_capital = models.CharField(max_length=32, blank=True, null=True, verbose_name='注册资本')
    established_date = models.DateTimeField(blank=True, null=True, default=None, verbose_name='成立日期')
    effective_start_date = models.DateTimeField(blank=True, null=True, default=None, verbose_name='营业期限(起)')
    effective_end_date = models.DateTimeField(blank=True, null=True, default=None, verbose_name='营业期限(止)')
    address = models.CharField(max_length=128, null=True, verbose_name='公司地址')
    city = models.CharField(max_length=32, null=True, verbose_name='所在城市')
    industry = models.CharField(max_length=32, null=True, verbose_name='所在行业')
    website = models.CharField(max_length=64, blank=True, null=True, verbose_name='企业网站')
    legal_person_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='企业法人姓名')
    legal_person_email = models.CharField(max_length=64, blank=True, null=True, verbose_name='企业法人邮箱')
    contact_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='联系人姓名')
    contact_tel = models.CharField(max_length=64, blank=True, null=True, verbose_name='联系人电话')
    contact_phone = models.CharField(max_length=64, blank=True, null=True, verbose_name='联系人手机号码')
    contact_email = models.CharField(max_length=64, blank=True, null=True, verbose_name='联系人邮箱')
    business_scope = models.TextField(max_length=256, blank=True, null=True, verbose_name='经营范围')
    remark = models.TextField(max_length=256, blank=True, null=True, verbose_name='备注')
    is_available = models.BooleanField(default=False, verbose_name='是否启用')  # 默认为还没激活

    objects = models.Manager()   # 默认模型管理器
    custom = EnterpriseManager()    # 自定义模型管理器，此管理器为返回的是is_delete=False的queryset

    class Meta:
        db_table = 'enterprise'  # 修改表名
        verbose_name = '企业信息表'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['account']  # 排序字段

    def __str__(self):
        return self.established_date + self.effective_start_date + self.effective_end_date
