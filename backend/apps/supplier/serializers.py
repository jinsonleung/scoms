from rest_framework import serializers
from rest_framework.response import Response

from apps.supplier.models import Supplier, SupplierContact
import django_filters
from django_filters.rest_framework import FilterSet


class SupplierContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierContact   # 序列化的对象名
        fields = '__all__'  # 序列化所有字段


class SupplierSerializer(serializers.ModelSerializer):
    # contact变量名必须是SupplierContact模型中外键的related_name
    contact = SupplierContactSerializer(many=True, read_only=True)
    # 自定义序列化字段，获取状态枚举值，对应get_status_label()自定义函数
    status_label = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Supplier   # 序列化的对象名
        # fields = '__all__'  # 序列化所有字段
        exclude = ['is_delete', 'create_datetime', 'create_by', 'update_datetime', 'update_by']
        depth = 2   # 指定深度

    # def create(self, validate_data):
    #
    #     print('validate_data=====')
    #
    #     # latest_account = validate_data['account']
    #     # validate_data['account'] = latest_account + 'ddd'
    #     # print('validate_data[account]', validate_data['account'])
    #     # # super.create(validate_data)
    #     # # contact_data = validate_data.pop('contact')
    #     # # supplier = self.create(**validate_data)
    #     # # return supplier
    #     # return Response({'msg': 'ok'})


    def get_status_label(self, obj):
        """ 获取状态数字对应的值
        自定义序列化字段，序列化的属性值由方法来提供
        方法的名：固定为get_属性名（self,obj）
        方法参数：序列化对象，序列化的model对象
        强烈建议：自定义序列化字段名不要与model已有的属性名相同
        """
        return obj.get_status_display()


class SupplierFilterSet(FilterSet):
    account = django_filters.CharFilter(field_name='account', lookup_expr="icontains")  # icontains 包含,忽略大小写
    full_name = django_filters.CharFilter(field_name='full_name', lookup_expr="icontains")  # icontains 包含,忽略大小写

    class Meta:
        model = Supplier  # 关联的模型
        fields = ['account', 'full_name']  # 过滤的字段



