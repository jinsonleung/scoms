from rest_framework import serializers
from apps.supplier.models import Supplier, SupplierContact
import django_filters
from django_filters.rest_framework import FilterSet


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

    def get_status(self, obj):
        return obj.get_status_display()



class SupplierFilterSet(FilterSet):
    """account、full_name字段的模糊查找过滤器"""
    account = django_filters.CharFilter(field_name='account', lookup_expr="icontains")  # icontains 包含,忽略大小写
    full_name = django_filters.CharFilter(field_name='full_name', lookup_expr="icontains")  # icontains 包含,忽略大小写

    class Meta:
        model = Supplier  # 关联的模型
        fields = ['account', 'full_name']  # 过滤的字段



