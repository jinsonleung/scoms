from django.db import models


# 企业及分支机构数据模型
class Enterprise(models.Model):
    id = models.SmallAutoField(primary_key=True, verbose_name='自增主键')
    account = models.CharField(max_length=16, unique=True, verbose_name='企业账号')
    full_name = models.CharField(max_length=64, blank=False, null=False, verbose_name='企业名全称')
    abbreviation_name = models.CharField(max_length=32, blank=False, null=False, verbose_name='企业名简称')
    classification = models.CharField(max_length=64, blank=False, null=False, verbose_name='企业分类（总部/分公司/子公司）')
    address = models.CharField(max_length=128, null=True, verbose_name='公司地址')
    city = models.CharField(max_length=32, null=True, verbose_name='所在城市')
    license_no = models.CharField(max_length=32,  null=True, verbose_name='营业执照号码')
    registration_date = models.DateTimeField(verbose_name='注册日期')
    registration_effect_start = models.DateTimeField(verbose_name='有效期开始日期')
    registration_effect_end = models.DateTimeField(verbose_name='有效期结束日期')
    industry = models.CharField(max_length=64, null=True, verbose_name='所在行业')
    legal_person_name = models.CharField(max_length=16, null=True, verbose_name='企业法人姓名')
    legal_person_email = models.CharField(max_length=64, null=True, verbose_name='企业法人邮箱')
    contact_tel = models.CharField(max_length=32, null=True, verbose_name='联系人电话')
    contact_phone = models.CharField(max_length=32, null=True, verbose_name='联系人手机号码')
    contact_email = models.CharField(max_length=64, null=True, verbose_name='联系人邮箱')
    remark = models.TextField(max_length=1024, null=True, verbose_name='备注')
    is_available = models.BooleanField(default=False, verbose_name='是否启用')  # 默认为还没激活
    is_delete = models.BooleanField(default=False, verbose_name='删除标志')  # 默认为还没删除
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='创建记录日期')   # 记录第一次创建时间，以后不会更新
    create_by = models.CharField(max_length=32, verbose_name='创建人')
    update_datetime = models.DateTimeField(auto_now=True, verbose_name='更新记录日期')   # 每次更新记录时就更新当前时间
    update_by = models.CharField(max_length=32, verbose_name='更新人')

    class Meta:  # 更改数据库表名称
        db_table = 'enterprise'  # 修改表名
        verbose_name = '企业及分支机构'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['account']  # 排序字段

    def __str__(self):
        return self.account
