from rest_framework import serializers
from rest_framework import exceptions
from demo.cars import models


# 群增群改辅助类（了解）
class BookListSerializer(serializers.ListSerializer):
    """
    1）create群增方法不需要重新
    2）update群改方法需要重写，且需要和views中处理request.data的逻辑配套使用
    3）self.child就代表该ListSerializer类绑定的ModelSerializer类
        BookListSerializer的self.child就是BookModelSerializer
    """

    # 重写update方法
    def update(self, queryset, validated_data_list):
        return [
            self.child.update(queryset[index], validated_data) for index, validated_data in
            enumerate(validated_data_list)
        ]


class CarModelSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        print(self.context)  # 可以获得视图类在初始化序列化对象时传入的context
        # self.context.update({'a': 10})  # 序列化类内部更新context，传递给视图类
        return attrs

    class Meta:
        # 配置自定义群增群改序列化类
        list_serializer_class = BookListSerializer

        model = models.Car
        fields = ['name', 'is_delete', 'price', 'brand', 'brand_', 'updated_time', 'sponsors_']

        extra_kwargs = {
            'brand': {
                'write_only': True,
            }
            # 'name':{
            #     'required':False
            # },
            # 'price': {
            #     'required': False
            # },
        }


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = ['name', 'is_delete', 'updated_time', 'car_list']