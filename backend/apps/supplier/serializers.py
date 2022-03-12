from rest_framework import serializers
from apps.supplier.models import Supplier, SupplierContact


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier   # 序列化的对象名
        # fields = '__all__'  # 序列化所有字段
        exclude = ['is_delete', 'create_datetime', 'create_by', 'update_datetime', 'update_by']


class SupplierContactSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()

    class Meta:
        model = SupplierContact   # 序列化的对象名
        fields = '__all__'  # 序列化所有字段
