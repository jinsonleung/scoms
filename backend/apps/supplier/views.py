from django.db.models import Q
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.supplier.models import Supplier, SupplierContact
from apps.supplier.serializers import SupplierSerializer, SupplierContactSerializer, SupplierFilterSet
from utils.pagination import Pagination
from rest_framework import mixins, exceptions
from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework


class SupplierModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Supplier.custom.all()    # 获取所有数据
    serializer_class = SupplierSerializer   # 序列化
    pagination_class = Pagination  # 分页
    # 配置模糊查询
    filter_backends = [DjangoFilterBackend]     # 查询配置
    filterset_class = SupplierFilterSet
    filter_fields = ['account', 'full_name']    # 查询字段



