from rest_framework import serializers
from apps.supplier.models import Supplier, SupplierContact


class SupplierContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierContact   # 序列化的对象名
        fields = '__all__'  # 序列化所有字段


class SupplierSerializer(serializers.ModelSerializer):
    # contact变量名必须是SupplierContact模型中外键的related_name
    contact = SupplierContactSerializer(many=True)

    class Meta:
        model = Supplier   # 序列化的对象名
        # fields = '__all__'  # 序列化所有字段
        exclude = ['is_delete', 'create_datetime', 'create_by', 'update_datetime', 'update_by']
        depth = 2   # 指定深度




