# Generated by Django 3.2.7 on 2022-01-27 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='effective_end_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='营业期限(止)'),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='effective_start_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='营业期限(起)'),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='established_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='成立日期'),
        ),
    ]
