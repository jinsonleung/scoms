from rest_framework import serializers
from apps.universalCode.airport.models import Airport


# 序列化器
class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport   # 序列化的对象名
        fields = '__all__'  # 序列化所有字段





