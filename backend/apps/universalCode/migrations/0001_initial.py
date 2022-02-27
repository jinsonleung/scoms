# Generated by Django 3.2.7 on 2022-02-26 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='国家英文全称')),
                ('chn_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='国家中文全称')),
                ('description', models.TextField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('is_delete', models.BooleanField(default=False, verbose_name='软删除标志')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建记录日期')),
                ('create_by', models.CharField(max_length=32, verbose_name='创建人')),
                ('update_datetime', models.DateTimeField(auto_now=True, db_index=True, verbose_name='更新记录日期')),
                ('update_by', models.CharField(max_length=32, verbose_name='更新人')),
            ],
            options={
                'verbose_name': '全球各洲表',
                'verbose_name_plural': '全球各洲表',
                'db_table': 'continent',
                'ordering': ['eng_name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso2_code', models.CharField(max_length=16, unique=True, verbose_name='国家两字码')),
                ('iso3_code', models.CharField(max_length=16, unique=True, verbose_name='国家三字码')),
                ('eng_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='国家英文')),
                ('full_eng_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='国家英文全称')),
                ('chn_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='国家中文')),
                ('full_chn_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='国家中文全称')),
                ('language', models.CharField(blank=True, max_length=64, null=True, verbose_name='所用语言')),
                ('phone_zone', models.CharField(blank=True, max_length=64, null=True, verbose_name='电话区号')),
                ('capital', models.CharField(blank=True, max_length=64, null=True, verbose_name='首都')),
                ('currency', models.CharField(blank=True, max_length=64, null=True, verbose_name='货币')),
                ('native', models.CharField(blank=True, max_length=128, null=True, verbose_name='种族')),
                ('emoji', models.CharField(blank=True, max_length=64, null=True, verbose_name='emoji')),
                ('emojiU', models.CharField(blank=True, max_length=128, null=True, verbose_name='emoji图标')),
                ('wiki_data_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='维基数据代码')),
                ('continent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universalCode.continent', verbose_name='所在洲id(外键)')),
                ('description', models.TextField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('is_delete', models.BooleanField(default=False, verbose_name='软删除标志')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建记录日期')),
                ('create_by', models.CharField(max_length=32, verbose_name='创建人')),
                ('update_datetime', models.DateTimeField(auto_now=True, db_index=True, verbose_name='更新记录日期')),
                ('update_by', models.CharField(max_length=32, verbose_name='更新人')),
            ],
            options={
                'verbose_name': '全球国家两字码表',
                'verbose_name_plural': '全球国家两字码表',
                'db_table': 'country',
                'ordering': ['iso2_code'],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso2_code', models.CharField(max_length=16, unique=True, verbose_name='省两字码')),
                ('eng_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='省英文全称')),
                ('chn_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='省中文全称')),
                ('country_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universalCode.country', verbose_name='所在国家id(外键)')),
                ('country_iso2_code', models.CharField(blank=True, max_length=32, null=True, verbose_name='国家代码')),
                ('fips_code', models.CharField(blank=True, max_length=64, null=True, verbose_name='fips代码')),
                ('wiki_data_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='维基数据代码')),
                ('description', models.TextField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('is_delete', models.BooleanField(default=False, verbose_name='软删除标志')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建记录日期')),
                ('create_by', models.CharField(max_length=32, verbose_name='创建人')),
                ('update_datetime', models.DateTimeField(auto_now=True, db_index=True, verbose_name='更新记录日期')),
                ('update_by', models.CharField(max_length=32, verbose_name='更新人')),
            ],
            options={
                'verbose_name': '全球各洲表',
                'verbose_name_plural': '全球各洲表',
                'db_table': 'state',
                'ordering': ['iso2_code'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso3_code', models.CharField(max_length=16, unique=True, verbose_name='城市三字码')),
                ('eng_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='城市英文全称')),
                ('chn_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='城市中文全称')),
                ('country_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universalCode.country', verbose_name='所在国家id')),
                ('country_iso2_code', models.CharField(blank=True, max_length=16, null=True, verbose_name='所在国家二字码')),
                ('state_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universalCode.state', verbose_name='所在省份id')),
                ('state_iso2_code', models.CharField(blank=True, max_length=16, null=True, verbose_name='所在省份二字码')),
                ('latitude', models.CharField(blank=True, max_length=64, null=True, verbose_name='纬度')),
                ('longitude', models.CharField(blank=True, max_length=64, null=True, verbose_name='经度')),
                ('wiki_data_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='维基数据代码')),
                ('description', models.TextField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('is_delete', models.BooleanField(default=False, verbose_name='软删除标志')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建记录日期')),
                ('create_by', models.CharField(max_length=32, verbose_name='创建人')),
                ('update_datetime', models.DateTimeField(auto_now=True, db_index=True, verbose_name='更新记录日期')),
                ('update_by', models.CharField(max_length=32, verbose_name='更新人')),
            ],
            options={
                'verbose_name': '全球城市三字码表',
                'verbose_name_plural': '全球城市三字码表',
                'db_table': 'city',
                'ordering': ['iso3_code'],
            },
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iata_code', models.CharField(max_length=16, unique=True, verbose_name='IATA机场代码')),
                ('icao_code', models.CharField(blank=True, max_length=16, null=True, verbose_name='ICAO机场代码')),
                ('eng_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='机场英文名称')),
                ('chn_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='机场中文名称')),
                ('country_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universalCode.country', verbose_name='所在国家')),
                ('country_iso2_code', models.CharField(blank=True, max_length=16, null=True, verbose_name='国家二字码')),
                ('city_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universalCode.city', verbose_name='所在城市id')),
                ('city_iso3_code', models.CharField(blank=True, max_length=16, null=True, verbose_name='城市三字码')),
                ('city_eng_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='城市英文名称')),
                ('city_chn_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='城市中文名称')),
                ('elevation', models.CharField(blank=True, max_length=64, null=True, verbose_name='海拨高度')),
                ('latitude', models.CharField(blank=True, max_length=64, null=True, verbose_name='纬度')),
                ('longitude', models.CharField(blank=True, max_length=64, null=True, verbose_name='经度')),
                ('time_zone', models.CharField(blank=True, max_length=64, null=True, verbose_name='时区')),
                ('utc', models.CharField(blank=True, max_length=16, null=True, verbose_name='UTC时差')),
                ('description', models.TextField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('is_delete', models.BooleanField(default=False, verbose_name='软删除标志')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建记录日期')),
                ('create_by', models.CharField(max_length=32, verbose_name='创建人')),
                ('update_datetime', models.DateTimeField(auto_now=True, db_index=True, verbose_name='更新记录日期')),
                ('update_by', models.CharField(max_length=32, verbose_name='更新人')),
            ],
            options={
                'verbose_name': '全球机场三字码表',
                'verbose_name_plural': '全球机场三字码表',
                'db_table': 'airport',
                'ordering': ['iata_code'],
            },
        ),
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iata_code', models.CharField(blank=True, max_length=16, null=True, verbose_name='IATA机场代码')),
                ('icao_code', models.CharField(blank=True, max_length=16, null=True, verbose_name='ICAO机场代码')),
                ('accounting_code', models.CharField(blank=True, max_length=16, null=True, verbose_name='ICAO机场代码')),
                ('airline_prefix_code', models.CharField(blank=True, max_length=16, null=True, verbose_name='ICAO机场代码')),
                ('eng_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='机场英文名称')),
                ('chn_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='机场中文名称')),
                ('call_sign', models.CharField(blank=True, max_length=64, null=True, verbose_name='机场英文名称')),
                ('country_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universalCode.country', verbose_name='所在国家id(外键)')),
                ('country_iso2_code', models.CharField(blank=True, max_length=16, null=True, verbose_name='国家二字码')),
                ('city_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universalCode.city', verbose_name='所在城市id(外键)')),
                ('city_ios3_code', models.CharField(blank=True, max_length=16, null=True, verbose_name='城市三字码')),
                ('description', models.TextField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('is_delete', models.BooleanField(default=False, verbose_name='软删除标志')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建记录日期')),
                ('create_by', models.CharField(max_length=32, verbose_name='创建人')),
                ('update_datetime', models.DateTimeField(auto_now=True, db_index=True, verbose_name='更新记录日期')),
                ('update_by', models.CharField(max_length=32, verbose_name='更新人')),
            ],
            options={
                'verbose_name': '全球航空公司二字码表',
                'verbose_name_plural': '全球航空公司二字码表',
                'db_table': 'airline',
                'ordering': ['iata_code'],
            },
        ),
    ]
