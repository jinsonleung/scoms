from django.db.models import Q
from rest_framework.response import Response
from apps.supplier.models import Supplier
from apps.supplier.serializers import SupplierSerializer
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

    def create_0(self, request, *args, **kwargs):
        """新增（正确）"""

        ext = str(request.FILES.get('files').name).split('.')[-1]
        fileName = 'hello.' + ext
        request.FILES.get('files').name = fileName
        # 获取前端表单数据
        data = request.data
        # 读取表单文件
        files = request.FILES.getlist('files')
        print('files==', files)
        fileNames = request.POST.get('fileNames')
        # 保存将表单文件文件到data
        for file in files:
            print('file=', type(file))
            data['business_licence_image'] = file
        # 获取最后一条记录所对应的供应商账号，如果空表则第1个账号为S00001+校验位
        try:
            latest_instance = self.get_queryset().latest('id')
            latest_account = getattr(latest_instance, 'account')
        except Supplier.DoesNotExist:
            latest_account = '00000'
        # 根据数据库中最后一个供应商账号自动生成新的账号
        new_account = create_new_supplier_account(latest_account)
        data['account'] = new_account
        # 反序列化并校验
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        # 保存至数据库
        serializer.save()
        # 返回数据给客户端
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response({'msg': 'okkkkk'})

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
        # 修改客户端营业执照文件名，格式为：账号_license_年月日时分秒_2位随机数
        file_extension = str(request.FILES.get('files').name).split('.')[-1]
        datetime_and_random_num = time.strftime('%Y%m%d%H%M%S')
        datetime_and_random_num = datetime_and_random_num + '_%d' % random.randint(0, 100)
        fileName = f'{new_account}_license_{datetime_and_random_num}.{file_extension}'
        # 获取前端表单数据（前端上传的营业执照只有仅限1张图片）
        data = request.data
        data['account'] = new_account
        data['business_licence_image'] = request.FILES.get('files')
        data['business_licence_image'].name = fileName
        # 反序列化并校验
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        # 保存至数据库
        serializer.save()
        # 返回数据给客户端
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response({'msg': 'okkkkk'})


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

    def update0(self, request, *args, **kwargs):
        # 1.获取id
        pk = kwargs.get('pk')
        # pk = 2
        # data = {
        #     "account": "000111",
        #     "full_name": "大疆公司"
        # }
        # 2.单改
        if pk:
            # 2.1 获取模型对象
            files = request.FILES
            print('==kwargs1==', request.data['business_licence_image'])
            print('==request.FILES==', request.FILES)
            print('==kwargs2==', files.get('business_licence_image'))

            try:
                instance = self.get_queryset().get(pk=pk)
            except Supplier.DoesNotExist:
                return Response(status.HTTP_404_NOT_FOUND)
            # 2.2 序列化
            # patrial=True就是将所有反序列化字段的required设置为False（提供就校验，不提供就不校验）
            serializer = SupplierSerializer(instance=instance,data=request.data, partial=True)
            # serializer = SupplierSerializer(instance=instance, data=data, partial=True)
            # 2.3 数据校验
            serializer.is_valid(raise_exception=True)
            # 2.4 保存数据
            serializer.save()
            # 2.5 返回结果给客户端
            return Response(serializer.data)

        else:
            return Response({'msg': 'okkkkkk'})

    def update(self, request, *args, **kwargs):
        """更新（正确）"""
        # 获取PK及数据
        pk = kwargs.get('pk')
        data = request.data
        # print('==data==', data)
        instance = self.get_queryset().get(pk=pk)
        files = request.FILES.getlist('files')
        fileNames = request.POST.get('fileNames')
        # print('==files==', files)
        print('==fileNames==', fileNames)
        data.pop('files')
        data.pop('fileNames')
        # print('==data==', data)

        for file in files:
            data['business_licence_image'] = file
            print('==data[business_licence_image]==', data['business_licence_image'])
            print('==data==', data)

            serializer = self.get_serializer(instance=instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'msg': 'okkkk'})









# https://www.jianshu.com/p/fc45221ba5fd
# https://blog.csdn.net/weixin_45407214/article/details/110124426