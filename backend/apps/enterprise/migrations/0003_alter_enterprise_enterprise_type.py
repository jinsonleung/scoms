# Generated by Django 4.0.2 on 2022-02-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0002_alter_enterprise_enterprise_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprise',
            name='enterprise_type',
            field=models.IntegerField(verbose_name='企业类型'),
        ),
    ]
