from django.db.models import Q
from rest_framework.response import Response
from apps.supplier.models import Supplier
from apps.supplier.serializers import SupplierSerializer
from utils.pagination import Pagination
from rest_framework import viewsets
from rest_framework import status


class SupplierModelViewSet(viewsets.ModelViewSet):
    """
    获取多条记录（可模糊查询）
    DRF过滤组件无法做到模糊"或逻辑"查询，要么重写过滤组件方法或使用以下Q组合模糊查询条件
    """
    queryset = Supplier.custom.all()    # 获取所有数据
    serializer_class = SupplierSerializer   # 序列化
    pagination_class = Pagination  # 分页

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
        # 1.获取id
        # pk = kwargs.get('pk')
        # pk = 2
        # data = {
        #     "account": "000111",
        #     "full_name": "大疆公司"
        # }
        print('==id==', request.POST.get('id'))
        pk = request.POST.get('id')
        # data = {
        #     "account": request.POST.get('account'),
        #     "full_name": request.POST.get('full_name'),
        #     "business_licence_image": request.FILES.get('business_licence_image'),
        # }
        # print('==data==', data)
        account = request.POST.get('account'),
        full_name = request.POST.get('full_name'),
        business_licence_image = request.POST.get('business_licence_image'),
        _obj = Supplier.objects.create(account=account, full_name=full_name, business_licence_image=business_licence_image)

        # 2.单改
        if pk:
            # 2.1 获取模型对象
            # files = request.FILES
            # print('==kwargs1==', request.data['business_licence_image'])
            # print('==request.FILES==', request.FILES)
            # print('==kwargs2==', files.get('business_licence_image'))

            try:
                instance = self.get_queryset().get(pk=pk)
            except Supplier.DoesNotExist:
                return Response(status.HTTP_404_NOT_FOUND)
            # 2.2 序列化
            # patrial=True就是将所有反序列化字段的required设置为False（提供就校验，不提供就不校验）
            serializer = SupplierSerializer(instance=instance, data=_obj, partial=True)
            # serializer = SupplierSerializer(instance=instance, data=data, partial=True)
            # 2.3 数据校验
            serializer.is_valid(raise_exception=True)
            # 2.4 保存数据
            serializer.save()
            # 2.5 返回结果给客户端
            return Response(serializer.data)

        else:
            return Response({'msg': 'okkkkkk'})
