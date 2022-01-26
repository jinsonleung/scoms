from rest_framework import serializers
from apps.customer.models import Customer


# 图书类序列货器
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer   # 序列化的对象名
        fields = '__all__'  # 序列货所有字段
