from rest_framework import serializers
from apps.universalCode.models import Country, City, Airport, Airline


# 序列化器
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country   # 序列化的对象名
        # fields = '__all__'  # 序列化所有字段
        exclude = ['is_delete', 'create_datetime', 'create_by', 'update_datetime', 'update_by']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City   # 序列化的对象名
        exclude = ['is_delete', 'create_datetime', 'create_by', 'update_datetime', 'update_by']


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport   # 序列化的对象名
        exclude = ['is_delete', 'create_datetime', 'create_by', 'update_datetime', 'update_by']


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline   # 序列化的对象名
        exclude = ['is_delete', 'create_datetime', 'create_by', 'update_datetime', 'update_by']







