from django.db import models
from apps.public.models import BaseModel
from apps.public.managers import CommonManager


class Status(models.IntegerChoices):
    """供应商使用状态枚举类型定义，单独一个类可以被不同的模型类使用"""
    NEW = 0, '新建'
    AVAILABLE = 1, '生效'
    UNAVAILABLE = 2, '失效'
    SUSPEND = 3, '冻结'


class Supplier(BaseModel):
    """
    供应商表，继承抽象基类BaseModel
    """
    status_choices = (
        (0, '新建'),
        (1, '生效'),
        (2, '失效'),
        (3, '冻结'),
    )

    account = models.CharField(max_length=16, blank=False, null=False, unique=True, verbose_name='账号')
    abbreviation_name = models.CharField(max_length=32, blank=True, null=True, verbose_name='简称')
    full_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='全称')
    architecture = models.CharField(max_length=64, blank=True, null=True, verbose_name='体系结构（总部/分公司/子公司）')
    unified_social_credit_code = models.CharField(max_length=32,  blank=True, null=True, verbose_name='统一社会信用代码')
    # 会将图片文件存放到media/supplierBusinessLicenceImage目录下，如果文件名重复则drf会自动添加缀
    business_licence_image = models.FileField(upload_to='supplierBusinessLicenceImage', blank=True, null=True, default='default.jpg', verbose_name='照业执照图片')
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
    banking_account_info = models.TextField(max_length=256, blank=True, null=True, verbose_name='银行对公账户')
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name='企业描述')
    status = models.IntegerField(choices=Status.choices, blank=False, null=False, verbose_name='状态')
    status_description = models.CharField(max_length=64, blank=True, null=True, verbose_name='状态说明')

    objects = models.Manager()   # 默认模型管理器
    custom = CommonManager()    # 自定义管理器

    class Meta:
        db_table = 'supplier'  # 数据库实际表名
        verbose_name = '供应商表'  # 详细表名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['id']  # 排序字段
        get_latest_by = 'account'

    def delete(self, using=None, keep_parents=False):
        """重写数据删除方法实现逻辑删除"""
        self.is_delete = True
        self.save()

    def __str__(self):
        """控制台对象输出内容"""
        # return '%s,%s' (self.account, self.full_name)
        return self.account

    # def image_img(self):
    #     print('==self.business_licence_image==', self.business_licence_image)
    #     if self.business_licence_image:
    #         return u'<img src="%s" width="50" height="50" />' % self.item_image.url
    #     else:
    #         return '(Sin imagen)'
    # image_img.short_description = 'Thumb'
    # image_img.allow_tags = True


class SupplierContact(models.Model):
    """供应商联系人表"""
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
    department = models.CharField(max_length=32, blank=False, null=False, verbose_name='部门名称')
    title = models.CharField(max_length=32, blank=True, null=True, verbose_name='职位')
    chn_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='中文名')
    eng_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='英文名')
    tel = models.CharField(max_length=128, blank=True, null=True, verbose_name='电话')
    phone = models.CharField(max_length=128, blank=True, null=True, verbose_name='手机')
    email = models.CharField(max_length=128, blank=True, null=True, verbose_name='邮箱')
    wechat = models.CharField(max_length=64, blank=True, null=True, verbose_name='微信号')
    qq = models.CharField(max_length=64, blank=True, null=True, verbose_name='QQ号')
    social_account = models.TextField(max_length=256, blank=True, null=True, verbose_name='其他社交账号')
    remark = models.TextField(max_length=256, blank=True, null=True, verbose_name='备注')
    supplier = models.ForeignKey(Supplier, blank=True, null=True, on_delete=models.CASCADE, related_name='contact',
                                 db_constraint=False, verbose_name='供应商id(外键)')  # 外键，断外键关联关系

    objects = models.Manager()  # 默认模型管理器

    class Meta:
        db_table = 'supplier_contact'  # 数据库实际表名
        verbose_name = '供应商联系人表'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['department']  # 排序字段

    def __str__(self):
        return '%s,%s' (self.department, self.chn_name)
