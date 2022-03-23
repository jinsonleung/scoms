from django.db.models import Q
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.supplier.models import Supplier, SupplierContact
from apps.supplier.serializers import SupplierSerializer, SupplierContactSerializer
from utils.pagination import Pagination
from rest_framework import mixins, exceptions
from rest_framework import generics
from rest_framework import viewsets


class SupplierModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Supplier.custom.all()    # 获取所有数据
    serializer_class = SupplierSerializer   # 序列化
    pagination_class = Pagination  # 分页


