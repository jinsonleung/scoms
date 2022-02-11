# Generated by Django 3.2.7 on 2022-02-11 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='address',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='公司地址'),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='unified_social_credit_code',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='统一社会信用代码'),
        ),
    ]
