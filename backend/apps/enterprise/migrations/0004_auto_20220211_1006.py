# Generated by Django 3.2.7 on 2022-02-11 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0003_auto_20220211_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='effective_end_date',
            field=models.DateField(blank=True, null=True, verbose_name='营业期限(止)'),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='effective_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='营业期限(起)'),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='established_date',
            field=models.DateField(blank=True, null=True, verbose_name='成立日期'),
        ),
    ]
