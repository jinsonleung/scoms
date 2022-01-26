from rest_framework import serializers
from apps.enterprise.models import Enterprise


# 图书类序列货器
class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise   # 序列化的对象名
        fields = '__all__'  # 序列货所有字段
