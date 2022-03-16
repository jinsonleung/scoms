'''
Author: Jinosn.Liang
Date: 2022-03-15 20:00:04
LastEditors: Jinson.Liang
LastEditTime: 2022-03-16 10:18:07
Description: 
FilePath: /backend/apps/student/views.py
'''
from django.http import Http404
from rest_framework.views import APIView
from apps.student.serializers import StudentSerializer
from apps.student.models import Student
from rest_framework.response import Response
from rest_framework import status


# 一、基本视图
class StudentAPIView(APIView):
    def get(self, request):
        """获取所有数据"""
        # 1.从数据库中获取所有记录
        students = Student.objects.all()
        # 2.序列化
        serializer = StudentSerializer(students, many=True)
        # 3.转换数据并返回给客户端
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        """添加一条记录"""

        print(f'request.data.get("name")={request.data.get("name")}')
        print(f'request.query_params={request.query_params}')

        return Response(status.HTTP_200_OK)

        # # 1.获取前端过来的数据
        # instance = request.data
        # # 2.反序列化
        # serializer = StudentSerializer(data=instance)
        # # 3.验证数据并保存到数据库
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # # 3.返回新增的模型数据给前端
        # return Response(serializer.data, status.HTTP_201_CREATED)


class StudentInfoAPIView(APIView):
    def get(self, request, pk):
        """获取一条记录"""
        # 1.从数据库获取一条记录
        try:
            instance = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        # 2. 序列化
        serializer = StudentSerializer(instance)
        # 3.返回数据给前端
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        """更新一条记录"""
        # 1.接收前端数据
        data = request.data
        # 2.查询数据库记录
        try:
            instance = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        # 2.序列化（核验并保存）
        serializer = StudentSerializer(instance, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 3.返回数据给前端
            return Response(serializer.data, status.HTTP_201_CREATED)
        return  Response(status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """删除一条"""
        # 1.接收前端数据
        try:
            instance = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        # 2.删除数据
        instance.delete()
        # 3.返回状态码
        return Response(status.HTTP_204_NO_CONTENT)

# 二、通用视图


# 三、混合视图

# 四、视图集

