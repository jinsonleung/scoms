from rest_framework.serializers import ModelSerializer
from demo.school.models import Student, Achievement


class AchievementModelSerializer(ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


class StudentModelSerializer(ModelSerializer):
    s_achievement = AchievementModelSerializer(many=True)

    class Meta:
        model = Student
        # fields = "__all__"
        fields = ['id', 'name', 's_achievement']


