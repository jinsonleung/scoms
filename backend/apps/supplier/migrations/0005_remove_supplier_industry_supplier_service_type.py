# Generated by Django 4.0.2 on 2022-04-19 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0004_alter_supplier_business_scope_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='industry',
        ),
        migrations.AddField(
            model_name='supplier',
            name='service_type',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='服务类型'),
        ),
    ]
