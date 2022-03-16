from rest_framework.serializers import ModelSerializer
from apps.student.models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {
            'age': {    # 字段限制，年龄不能超过28岁，**此不起作用
                'max_value': 28,
                'error_messages': {
                    'max_value': '年龄不能超过28岁！',
                }
            }
        }
