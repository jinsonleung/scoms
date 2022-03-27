from django.db.models import Q
from rest_framework.response import Response
from apps.supplier.models import Supplier
from apps.supplier.serializers import SupplierSerializer
from utils.pagination import Pagination
from rest_framework import viewsets


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


