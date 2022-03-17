'''
Author: Jinosn.Liang
Date: 2022-03-15 20:00:04
LastEditors: Jinson.Liang
LastEditTime: 2022-03-16 10:18:07
Description: 
FilePath: /backend/apps/student/views.py
'''
from rest_framework.views import APIView
from demo.student.serializers import StudentSerializer
from demo.student.models import Student
from rest_framework.response import Response
from rest_framework import status


"""
GET /demo/student/ 获取所有记录
POST /demo/student/ 添加一条记录

GET /demo/student/<pk>  获取一条记录
PUT /demo/student/<pk>   更新一条学生记录
DELETE /demo/student/<pk>   删除一条学生记录
"""


# 一、基本视图类
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
        # 1.获取前端过来的数据
        instance = request.data
        # 2.反序列化
        serializer = StudentSerializer(data=instance)
        # 3.验证数据并保存到数据库
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 3.返回新增的模型数据给前端
        return Response(serializer.data, status.HTTP_201_CREATED)


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

from rest_framework.generics import GenericAPIView


# 二、通用视图类
class StudentGenericAPIView(GenericAPIView):
    # 配置GenericAPIView属性serializer_class,queryset
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get(self, request):
        """获取所有记录"""
        # 1.从数据库从查询所有记录
        instances = self.get_queryset()
        # 2.序列化
        serializer = self.get_serializer(instances, many=True)
        # 3.返回给前端
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """添加一条记录"""
        # 1.获取前端数据
        data = request.data
        # 2.反序列化
        serializer = self.get_serializer(data=data)
        # 3. 数据核验并保存到数据
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 4.返回数据给前端
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentInfoGenericAPIView(GenericAPIView):
    # 配置GenericAPIVie两个属性值
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get(self, request, pk):
        """获取一条记录"""
        # 1.根据参数pk，查询数据库获取一条记录
        # 下面一名相当于instance = self.get_queryset().get(pk=pk)
        # print(f'request.query_params={request.query_params}')
        instance = self.get_object()
        # 2.序列化
        serializer = self.get_serializer(instance)
        # 3.返回给前端
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """修改一条记录"""
        # 1.获取数据库一条记录
        instance = self.get_object()
        # 2.获取前端数据
        data = request.data
        # 3.序列化
        serializer = self.get_serializer(instance, data=data)
        # 4.校验数据并保存到数据库
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 5.返回结果给前端
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        """删除一条记录"""
        # 1.从数据库中获取一条记录
        instance = self.get_object()
        # 2.删除记录
        instance.delete()
        # 返回404给前端
        return Response(status.HTTP_204_NO_CONTENT)


# 三、扩展视图类（混入视图类）
"""
from rest_framework.mixins import ListModelMixin    获取多条数据，返回响应结果 list
from rest_framework.mixins import CreateModelMixin  添加一条数据，返回响应结果   create
from rest_framework.mixins import RetrieveModelMixin    获取一条数据，返回响应结果   retrieve
from rest_framework.mixins import UpdateModelMixin  更新一条数据，返回响应结果   update（更新全部字段）和partial_update（更新单个或部分字段，如修改密码、修改头像）
from rest_framework.mixins import DetroyModelMixin  删除一条数据，返回响应结果   destroy
"""

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class StudentMixinAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        print(f'request._request.META={request._request.META["REMOTE_ADDR"]}')
        return self.list(request)

    def post(self, request):
        return self.create(request)


class StudentInfoMixinAPIView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# 四、视图子类
"""
视图子类是通用视图类 和 扩展视图类的 子类，提供各种视图方法调用mixins操作
1.ListAPIView = GenericAPIView + ListModelMixin   # 获取所有记录
2.CreateAPIView = GenericAPIView + CreateModelMixin   # 添加一条记录
3.RetrieveAPIView = GenericAPIView + RetrieveModelMixin   # 获取一条记录 
4.UpdateAPIView = GenericAPIView + UpdateModelMixin   # 更新一条记录
5.DestroyAPIView = GenericAPIView + DestroyModelMixin # 删除一条记录
6.ListCreateAPIView = ListAPIView + CreateAPIView 
7.RetrieveUpdateAPIView = RetrieveAPIView + UpdateAPIView
8.RetrieveDestroyAPIVIEW = RetrieveAPIView + DestroyAPIView
9.RetrieveUpdateDestroyAPIView = RetrieveAPIView + UpdateAPIView + DestroyAPIView 
"""

from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView


# class StudentView(ListAPIView, CreateAPIView):
class StudentView(ListCreateAPIView):
    """获取所有记录、添加一条记录"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# class StudentInfoView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
class StudentInfoView(RetrieveUpdateDestroyAPIView):
    """获取一条记录、更新一条记录、删除一条记录"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
