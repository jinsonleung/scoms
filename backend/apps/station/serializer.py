from rest_framework import serializers
from apps.station.models import Station


# 图书类序列货器
class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station   # 序列化的对象名
        fields = '__all__'  # 序列货所有字段

