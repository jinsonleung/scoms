from rest_framework import serializers
from apps.universalCode.models import Continent, State, Country, City, Airport, Airline


class UniversalCodeSerializer(serializers.ModelSerializer):
    pass


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent   # 序列化的对象名
        # fields = '__all__'  # 序列化所有字段
        exclude = ['is_delete', 'create_datetime', 'create_by', 'update_datetime', 'update_by']


class CountrySerializer(serializers.ModelSerializer):
    continent = ContinentSerializer()

    class Meta:
        model = Country   # 序列化的对象名
        # fields = '__all__'  # 序列化所有字段
        exclude = ['is_delete', 'create_datetime', 'create_by', 'update_datetime', 'update_by']


class StateSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = State   # 序列化的对象名
        # fields = '__all__'  # 序列化所有字段
        exclude = ['is_delete', 'create_datetime', 'create_by', 'update_datetime', 'update_by']


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    state = StateSerializer()

    class Meta:
        model = City   # 序列化的对象名
        exclude = ['is_delete', 'create_datetime', 'create_by', 'update_datetime', 'update_by']


class AirportSerializer(serializers.ModelSerializer):
    """
    参考：https://www.5axxw.com/questions/content/xbebfr
    """
    country = CountrySerializer()
    city = CitySerializer()

    class Meta:
        model = Airport   # 序列化的对象名
        # fields = '__all__'  # 序列化所有字段
        exclude = ['is_delete', 'create_datetime', 'create_by', 'update_datetime', 'update_by']


class AirlineSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    city = CitySerializer()

    class Meta:
        model = Airline   # 序列化的对象名
        exclude = ['is_delete', 'create_datetime', 'create_by', 'update_datetime', 'update_by']







