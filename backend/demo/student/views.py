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


# 1、基本视图类
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


from rest_framework.generics import GenericAPIView


# 2、通用视图类
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


# 3、扩展视图类（混入视图类）
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


# 4、视图子类
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


"""
上述视图子类代码中也存在相同代码情况，如果需要合并同一个接口，则需考虑以下两个问题：
1.路由合并问题
2.get方法重复问题
DRF提供了视图集，用来解决上述问题
"""


# 5、视图集
"""
1.普通视图集ViewSet，解决了APIView代码重复问题，可以将CRUD5个接口封装在一个类中
2.通用视图集GenericViewSet，解决了APIView代码重复问题，可以将CRUD5个接口封装在一个类中，让代码更通用
3.能用视图集+混入视图，GenericViewSet+Mixin，可更简化代码
"""

"""5.1 普通视图集"""
from rest_framework.viewsets import ViewSet


class StudentViewSet(ViewSet):
    """普通视图集，五个接口封装在一个类中"""
    def get_student_list(self, request):
        """获取所有数据"""
        # 1.从数据库中获取所有记录
        students = Student.objects.all()
        # 2.序列化
        serializer = StudentSerializer(students, many=True)
        # 3.转换数据并返回给客户端
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):
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

    def get_student(self, request, pk):
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

    def update(self, request, pk):
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

"""5.2 通用视图集"""
from rest_framework.viewsets import GenericViewSet

class StudentGenericViewSet(GenericViewSet):
    # 通用视图集，配置GenericAPIVie两个属性值
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def list(self, request):
        """获取所有记录"""
        # 1.从数据库从查询所有记录
        instances = self.get_queryset()
        # 2.序列化
        serializer = self.get_serializer(instances, many=True)
        # 3.返回给前端
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
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

    def get_student(self, request, pk):
        """获取一条记录"""
        # 1.根据参数pk，查询数据库获取一条记录
        # 下面一名相当于instance = self.get_queryset().get(pk=pk)
        # print(f'request.query_params={request.query_params}')
        instance = self.get_object()
        # 2.序列化
        serializer = self.get_serializer(instance)
        # 3.返回给前端
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
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

    def destroy(self, request, pk):
        """删除一条记录"""
        # 1.从数据库中获取一条记录
        instance = self.get_object()
        # 2.删除记录
        instance.delete()
        # 返回404给前端
        return Response(status.HTTP_204_NO_CONTENT)

"""5.3 通用视图集+混入视图"""
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class StudentMixinGenericViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    # 通用视图集，配置GenericAPIVie两个属性值
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


"""5.4 ReadonlyModelViewSet
1）5.3 中的GenericViewSet+Mixin视图集所继承的类太多，使用ReadOnlyModelViewSet取代，获取多条记录或一条记录
2）ReadOnlyModelViewSet=GenericViewSet+Mixins.ListModelMixin+Mixins.RetrieveModelMixin
"""

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin

class StudentReadOnlyModelViewSet(ReadOnlyModelViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    """查询所有记录或一条记录"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


"""5.5 ModelViewSet(万能视图集，最终版)
1）5.4 ReadOnlyModelViewSet+Mixin视图集所继承的类还是有4个，使用ModelViewSet取代，实现全部5个接口
"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # ● 路由对象给视图集生成路由信息时，只会生成5个基本api接口，这主要是router只识别5个混入类的原因
    # ● 我们开发中自定义的视图方法，路由对象不会自动生成路由信息
    # ● 在视图集中，如果要让Router自动帮我们为自定义的动作生成路由信息，需要使用到rest_framework.decortions.action装饰器
    # ● 在视图集中，比普通视图多了一个action属性
    # ● 以下我们在视图集中自定义的这个login方法，如果希望被外界访问到，则必须通过action装饰器告诉路由对象给它生成一个路由信息


    # ● action装饰器可以接收至少两个参数：
    #   methods：声明action对应的请求方式，列表参数
    #   detail：声明该action路径是否与单一资源对应，布值
    #       ■ True：表示的路径是xxx / < pk > / action方法名 /，如students / 20 / login /
    #       ■ False：表示的路径是xxx / action方法名 /，如students / login /
    #  url_path：声明该action的路由尾缀，如设置url_path = 'user/login，则url为 http://127.0.0.1:8000/student/10/user/login/
    @action(methods=['get'], detail=False)
    def login(self, reqeust):
        """
        自定义方法，此url为：http://127.0.0.1:8000/student/login/
        self.method 获得本次客户端的http请求
        self.action 获得本闪客户端请求的视图方法名（由ViewSet提供）
        """
        return Response({'msg': '注册成功！'})

    @action(methods=['get'], detail=True)
    def login_log(self, reqeust, pk):
        """
        自定义方法，此url为：http://127.0.0.1:8000/demo/student10/18/login_log/
        """
        print(f'self.action={self.action}')  # self.action=login_log
        return Response({'msg': '用户登录历史记录'})

    @action(methods=['get'], detail=True, url_path='login/log')
    def login_log2(self, reqeust, pk):
        """
        自定义方法，此url为：http://127.0.0.1:8000/demo/student10/18/login/log/
        """
        return Response({'msg': '用户登录历史记录2'})
