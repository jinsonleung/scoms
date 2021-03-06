# Generated by Django 3.2.7 on 2022-02-09 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='软删除标志')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建记录日期')),
                ('create_by', models.CharField(max_length=32, verbose_name='创建人')),
                ('update_datetime', models.DateTimeField(auto_now=True, db_index=True, verbose_name='更新记录日期')),
                ('update_by', models.CharField(max_length=32, verbose_name='更新人')),
                ('id', models.SmallAutoField(primary_key=True, serialize=False, verbose_name='自增主键')),
                ('superior_level', models.CharField(blank=True, max_length=64, null=True, verbose_name='上级企业')),
                ('account', models.CharField(max_length=16, unique=True, verbose_name='企业账号')),
                ('full_name', models.CharField(max_length=64, verbose_name='企业名全称')),
                ('abbreviation_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='企业名简称')),
                ('enterprise_type', models.CharField(max_length=16, verbose_name='企业类型')),
                ('architecture', models.CharField(max_length=64, verbose_name='体系结构（总部/分公司/子公司）')),
                ('unified_social_credit_code', models.CharField(max_length=32, null=True, verbose_name='统一社会信用代码')),
                ('registered_capital', models.CharField(blank=True, max_length=32, null=True, verbose_name='注册资本')),
                ('established_date', models.DateField(blank=True, default=None, null=True, verbose_name='成立日期')),
                ('effective_start_date', models.DateField(blank=True, default=None, null=True, verbose_name='营业期限(起)')),
                ('effective_end_date', models.DateField(blank=True, default=None, null=True, verbose_name='营业期限(止)')),
                ('address', models.CharField(max_length=128, null=True, verbose_name='公司地址')),
                ('city', models.CharField(blank=True, max_length=64, null=True, verbose_name='所在城市')),
                ('industry', models.CharField(blank=True, max_length=32, null=True, verbose_name='所在行业')),
                ('website', models.CharField(blank=True, max_length=64, null=True, verbose_name='企业网站')),
                ('legal_person_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='企业法人姓名')),
                ('legal_person_email', models.CharField(blank=True, max_length=64, null=True, verbose_name='企业法人邮箱')),
                ('contact_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='联系人姓名')),
                ('contact_tel', models.CharField(blank=True, max_length=64, null=True, verbose_name='联系人电话')),
                ('contact_phone', models.CharField(blank=True, max_length=64, null=True, verbose_name='联系人手机号码')),
                ('contact_email', models.CharField(blank=True, max_length=64, null=True, verbose_name='联系人邮箱')),
                ('business_scope', models.TextField(blank=True, max_length=256, null=True, verbose_name='经营范围')),
                ('remark', models.TextField(blank=True, max_length=256, null=True, verbose_name='备注')),
                ('is_available', models.BooleanField(default=False, verbose_name='是否启用')),
            ],
            options={
                'verbose_name': '企业信息表',
                'verbose_name_plural': '企业信息表',
                'db_table': 'enterprise',
                'ordering': ['account'],
            },
        ),
    ]
