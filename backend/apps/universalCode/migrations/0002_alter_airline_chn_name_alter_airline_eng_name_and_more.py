# Generated by Django 4.0.2 on 2022-02-22 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universalCode', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='chn_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='机场中文名称'),
        ),
        migrations.AlterField(
            model_name='airline',
            name='eng_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='机场英文名称'),
        ),
        migrations.AlterField(
            model_name='airport',
            name='chn_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='机场中文名称'),
        ),
        migrations.AlterField(
            model_name='airport',
            name='eng_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='机场英文名称'),
        ),
        migrations.AlterField(
            model_name='city',
            name='chn_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='城市中文全称'),
        ),
        migrations.AlterField(
            model_name='city',
            name='eng_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='城市英文全称'),
        ),
        migrations.AlterField(
            model_name='country',
            name='chn_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='国家中文全称'),
        ),
        migrations.AlterField(
            model_name='country',
            name='eng_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='国家英文全称'),
        ),
    ]