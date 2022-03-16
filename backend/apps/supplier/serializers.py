from rest_framework import serializers
from apps.supplier.models import Supplier, SupplierContact


class SupplierContactSerializer(serializers.ModelSerializer):
    # supplier = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    supplier = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = SupplierContact   # 序列化的对象名
        fields = '__all__'  # 序列化所有字段


class SupplierSerializer(serializers.ModelSerializer):
    # supplierContact = SupplierContactSerializer(many=True, read_only=True)
    # supplierContact = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Supplier   # 序列化的对象名
        # fields = '__all__'  # 序列化所有字段
        exclude = ['is_delete', 'create_datetime', 'create_by', 'update_datetime', 'update_by']



