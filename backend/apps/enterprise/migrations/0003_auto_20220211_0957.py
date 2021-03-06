# Generated by Django 3.2.7 on 2022-02-11 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0002_auto_20220211_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='architecture',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='体系结构（总部/分公司/子公司）'),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='enterprise_type',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='企业类型'),
        ),
    ]
