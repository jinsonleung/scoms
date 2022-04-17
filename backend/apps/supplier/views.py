from django.db.models import Q
from rest_framework.response import Response
from apps.supplier.models import Supplier, SupplierContact
from apps.supplier.serializers import SupplierSerializer, SupplierContactSerializer
from utils.pagination import Pagination
from rest_framework import viewsets
from rest_framework import status
import random
import time


def create_new_supplier_account(latest_account):
    """
    自动生成供应商账号
    供应商账号生成规则：由S+5位账号+1位校验位
    """
    # 截取5位账号
    latest_account_num = latest_account[1:6]
    # 将5位账号字符串转为数据加1，不足5位前补上0
    new_account_num = str((int(latest_account_num)+1)).zfill(5)
    # 系数
    coefficient = [5, 2, 4, 1, 3]
    # 取模种子数组
    mod_digital = [1, 0, 9, 8, 7, 6, 5, 4, 3, 2]
    # 每位系系统与每位账号相乘后求和
    _sum = 0
    for i in range(5):
        _sum += int(coefficient[i])*int(new_account_num[i])
    # 取模并得到校验位
    mod_num = _sum % 10
    validate_num = mod_digital[mod_num]
    # 拼接下一个账号
    new_account = "S" + new_account_num + str(validate_num)
    return new_account


class SupplierModelViewSet(viewsets.ModelViewSet):
    """
    获取多条记录（可模糊查询）
    DRF过滤组件无法做到模糊"或逻辑"查询，要么重写过滤组件方法或使用以下Q组合模糊查询条件
    """
    queryset = Supplier.custom.all()    # 获取所有数据
    serializer_class = SupplierSerializer   # 序列化
    pagination_class = Pagination  # 分页

    def create(self, request, *args, **kwargs):
        """新增（正确）"""
        # 获取最后一条记录所对应的供应商账号，如果空表则第1个账号为S00001+校验位
        try:
            latest_instance = self.get_queryset().latest('id')
            latest_account = getattr(latest_instance, 'account')
        except Supplier.DoesNotExist:
            latest_account = '00000'
        # 根据数据库中最后一个供应商账号自动生成新的账号
        new_account = create_new_supplier_account(latest_account)
        print('==new_account==', new_account)
        data = request.data
        # request数据不可修改，变量设置为_mutable=True，即可更改
        data._mutable = True
        data['account'] = new_account
        image_file = request.FILES.get('files')
        if image_file:
            file_extension = str(image_file.name).split('.')[-1]
            datetime_and_random_num = time.strftime('%Y%m%d%H%M%S')
            datetime_and_random_num = datetime_and_random_num + '_%d' % random.randint(0, 100)
            new_image_file_name = f'{new_account}_LICENSE_{datetime_and_random_num}.{file_extension}'
            image_file.name = new_image_file_name
            data['business_licence_image'] = image_file
        else:
            data.pop('business_licence_image')
        #     image_file.name = 'supplierBusinessLicenceImage/default.jpg'
        # data['business_licence_image'] = image_file
        data._mutable = False
        # 反序列化并校验
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        # 保存至数据库
        serializer.save()
        # 返回数据给客户端
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'msg': 'okkkkk'})

    def list(self, request, *args, **kwargs):
        """重写list，实现供应商账号、供应商名称模糊查询"""
        # 获取查询参数字符串
        queryText = request.query_params.get('queryText')
        if queryText != '':
            # 模糊查询，拼接Q组合模糊查询条件，icontains中的’i’表示忽略大小写；contains则区分大小写
            query_criteria = Q(account__icontains=queryText) | Q(full_name__icontains=queryText)
            queryset = self.get_queryset().filter(query_criteria)
        else:
            # 没有模糊查询
            queryset = self.filter_queryset(self.get_queryset())
        # 分页、序列化并返回数据级前端
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        # 若没有分页，则序列化返回数据给前端
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """更新（正确）"""
        # 获取PK及数据
        pk = kwargs.get('pk')
        instance = self.get_queryset().get(pk=pk)
        data = request.data
        data._mutable = True
        account = data.get('account')
        data.pop('files')
        data.pop('fileNames')
        image_file = request.FILES.get('files')
        if image_file:
            # 文件重新命名
            file_extension = str(image_file.name).split('.')[-1]
            datetime_and_random_num = time.strftime('%Y%m%d%H%M%S')
            datetime_and_random_num = datetime_and_random_num + '_%d' % random.randint(0, 100)
            new_image_file_name = f'{account}_LICENSE_{datetime_and_random_num}.{file_extension}'
            image_file.name = new_image_file_name
            data['business_licence_image'] = image_file
        else:
            data.pop('business_licence_image')
        data._mutable = False
        serializer = self.get_serializer(instance=instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response({'msg': 'okkkk'})


class SupplierContactViewSet(viewsets.ModelViewSet):
    queryset = SupplierContact.objects.all()    # 获取所有数据
    serializer_class = SupplierContactSerializer   # 序列化
    # pagination_class = Pagination  # 分页
    pagination_class = None  # 分页







# https://www.jianshu.com/p/fc45221ba5fd
# https://blog.csdn.net/weixin_45407214/article/details/110124426