from django.db.models import Q
from django.http import JsonResponse
from rest_framework.response import Response
from apps.supplier.models import Supplier
from apps.supplier.serializers import SupplierSerializer
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
            query_criteria = Q(account__icontains=queryText) | Q(abbreviation_name__icontains=queryText) | Q(full_name__icontains=queryText)
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

    def put(self, request, *args, **kwargs):
        """提供全部数据，单改"""
        request_data = request.data
        pk = kwargs.get('pk')
        print('==put PK==', pk)
        try:
            current_obj = Supplier.objects.filter(pk=pk, is_delete=False).first()
            if not current_obj:
                raise exceptions.ValidationError('数据错误')
        except:
            return Response({
                'status': 1,
                'msg': '数据错误'
            })
        # 需要进行update时,要同时传入instance和data
        obj_serial = SupplierSerializer(instance=current_obj, data=request_data)
        obj_serial.is_valid(raise_exception=True)
        new_obj = obj_serial.save()
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': SupplierSerializer(instance=new_obj).data
        })

    def delete(self, request, *args, **kwargs):
        """单删及群删"""
        pk = kwargs.get('pk')
        print('==delete PK==', pk)
        if pk:
            delete_obj = Supplier.objects.filter(pk=pk, is_delete=False).update(is_delete=True)
        else:
            pks = request.data.get('pks')
            delete_obj = Supplier.objects.filter(pk__in=pks, is_delete=False).update(is_delete=True)
        if delete_obj:
            return Response({
                'status': 0,
                'msg': '删除成功'
            })
        return Response({
            'status': 1,
            'msg': '删除失败'
        })