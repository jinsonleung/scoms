from django.db.models import Q
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.supplier.models import Supplier, SupplierContact
from apps.supplier.serializers import SupplierSerializer, SupplierContactSerializer
from utils.pagination import Pagination
from rest_framework import mixins, exceptions
from rest_framework import generics


class SupplierList(generics.ListAPIView):
    """列出所有的记录，或创建一条新的记录"""
    queryset = Supplier.custom.all()  # 获取非软删、除的记录
    serializer_class = SupplierSerializer  # 序列化
    pagination_class = Pagination  # 分页

    def get(self, request, *args, **kwargs):
        print('==国家多条件查询==', request)
        queryText = request.query_params.get('queryText')
        if queryText != '':
            # Q组合模糊查询，icontains中的’i’表示忽略大小写；contains则区分大小写
            query_criteria = Q(iso2_code__icontains=queryText) | Q(iso3_code__icontains=queryText) | Q(chn_name__icontains=queryText) | Q(continent__chn_name__icontains=queryText)
            query_result = Supplier.custom.filter(query_criteria)
            page = self.paginate_queryset(query_result)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(query_result, many=True)
            return Response(serializer.data)
        return self.list(request, *args, **kwargs)


class SupplierDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    """获取、更新或删除一条记录"""
    # queryset = Supplier.objects.all()   # 获取所有记录
    queryset = Supplier.custom.all()  # 获取非软删除的记录
    serializer_class = SupplierSerializer

    def get(self, request, *args, **kwargs):
        """单查"""
        print('==单查==', request)
        return self.retrieve(request, *args, **kwargs)
