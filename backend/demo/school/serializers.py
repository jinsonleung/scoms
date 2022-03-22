from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from demo.school.models import Student, Achievement, Course, Teacher

"""
嵌套序列化器使用
"""


class TeacherModelSerializer(ModelSerializer):
    """老师序列化器"""
    class Meta:
        model = Teacher
        fields = '__all__'
        # fields = ['name']


class CourseModelSerializer(ModelSerializer):
    """课程序列化器"""
    # 嵌套数据对应的只有一条时则不需要加many=True
    teacher = TeacherModelSerializer()

    class Meta:
        model = Course
        # fields = '__all__'
        fields = ['id', 'name', 'teacher']
        # fields = ['name']


# 方法一：直接嵌套
class Achievement1ModelSerializer(ModelSerializer):
    """
    课程分数序列化器
    """
    # 嵌套数据对应的只有一条时则不需要加many=True
    course = CourseModelSerializer()

    class Meta:
        model = Achievement
        # 可以控制序列化输出的字段，外键使用"course_id"与"course"是一样的
        # fields = '__all__'
        fields = ['id', 'course', 'score', 'create_datetime']


# 方法二：语句嵌套序列化器，source方式
class Achievement2ModelSerializer(ModelSerializer):
    """
    课程分数序列化器，语句嵌套
    """
    course_name = serializers.CharField(source='course.name')
    teacher_name = serializers.CharField(source='course.teacher.name')

    class Meta:
        model = Achievement
        fields = ['id', 'course_name', 'teacher_name', 'score', 'create_datetime']


# 方法三：指定关系深度属性
class Achievement3ModelSerializer(ModelSerializer):
    """
    课程分数序列化器，语句嵌套
    """

    class Meta:
        model = Achievement
        fields = '__all__'
        # 指定深度
        # 成绩->课程  深度为1
        # 成绩->课程->老师  深度为2
        depth = 2   # 深度属性


class StudentModelSerializer(ModelSerializer):
    """
    学生序列化器
    学生：课程分数 => 1:n
    学生表为主表，课程分数表为子表，通过主表获取子表数据
    """
    # s_achievement必须为外键字段，非外键字段不能给序列化器
    # 嵌套数据有多条时须加上many=True，只有一条时则不需要加
    # s_achievement = Achievement1ModelSerializer(many=True)   # 方法一：直接嵌套
    # s_achievement = Achievement2ModelSerializer(many=True)  # 方法二: 语句嵌套，Source指定
    # s_achievement = Achievement3ModelSerializer(many=True)  # 方法三: 指定关系深度属性

    class Meta:
        model = Student # 方法一、二和三使用
        # fields = "__all__"
        # s_achievement为外键的related_name
        # fields = ['id', 'name', 'sex', 's_achievement']   # 方法一
        # fields = ['id', 'name', 'sex', 's_achievement']   # 方法二
        # fields = ['id', 'name', 'sex', 's_achievement']     # 方法三
        fields = ['id', 'name', 'sex', 'achievement']     # 方法四，模型属性


