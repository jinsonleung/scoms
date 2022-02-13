from django.http import QueryDict, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from utils.pagination import Pagination
from apps.enterprise.models import Enterprise
from apps.enterprise.serializers import EnterpriseSerializer
from rest_framework import mixins, status, exceptions
from rest_framework import generics
import json
from django.views.decorators.csrf import csrf_exempt  # 取消csrf校验


class EnterpriseList(generics.ListAPIView, mixins.CreateModelMixin, generics.GenericAPIView):
    """列出所有的记录，或创建一条新的记录"""
    # queryset = Enterprise.objects.all()   # 获取所有记录
    queryset = Enterprise.custom.all()  # 获取非软删、除的记录
    serializer_class = EnterpriseSerializer  # 序列化
    pagination_class = Pagination  # 分页

    def get(self, request, *args, **kwargs):
        """群查，获取分页数据"""
        json_data = {"message": "ok", "errorCode": 0, "data": {}}
        objs = Enterprise.custom.all()
        if not objs:
            return Response({
                'status': 1,
                'msg': '请求资源不存在'
            })
        # objs_serial = EnterpriseSerializer(instance=objs, many=True).data
        json_data = EnterpriseSerializer(instance=objs, many=True).data
        return Response(json_data)
        # return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """单增及群增"""
        request_data = request.data
        if isinstance(request_data, dict):
            many = False
        elif isinstance(request_data, list):
            many = True
        else:
            raise exceptions.ValidationError('数据格式不正确')
        obj_serial = EnterpriseSerializer(data=request_data, many=many)
        obj_serial.is_valid(raise_exception=True)
        obj_result = obj_serial.save()
        # 获取序列化数据
        obj_data = EnterpriseSerializer(instance=obj_result, many=many).data
        return JsonResponse(obj_data)


class EnterpriseDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    """获取、更新或删除一条记录"""
    # queryset = Enterprise.objects.all()   # 获取所有记录
    queryset = Enterprise.custom.all()  # 获取非软删除的记录
    serializer_class = EnterpriseSerializer

    def get(self, request, *args, **kwargs):
        """单查"""
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """提供全部数据，单改"""
        request_data = request.data
        pk = kwargs.get('pk')
        print('==put PK==', pk)
        try:
            current_obj = Enterprise.objects.filter(pk=pk, is_delete=False).first()
            if not current_obj:
                raise exceptions.ValidationError('数据错误')
        except:
            return Response({
                'status': 1,
                'msg': '数据错误'
            })
        # 需要进行update时,要同时传入instance和data
        obj_serial = EnterpriseSerializer(instance=current_obj, data=request_data)
        obj_serial.is_valid(raise_exception=True)
        new_obj = obj_serial.save()
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': EnterpriseSerializer(instance=new_obj).data
        })

    # def patch(self, request, *args, **kwargs):
    #     """提供局部数据，单改或多改"""
    #     request_data = request.data
    #     pk = kwargs.get('pk')
    #     pks = []
    #     update_data = []
    #     if pk and isinstance(request_data, dict):
    #         pks = [pk, ]
    #         update_data = [request_data, ]
    #     elif not pk and isinstance(request_data, list):
    #         for dic in request_data:
    #             pks.append(dic.pop('pk'))
    #             update_data.append(dic)
    #     else:
    #         return Response({
    #             'status': 1,
    #             'msg': '数据格式错误'
    #         })
    #     if not pks or not update_data:
    #         return Response({
    #             'status': 1,
    #             'msg': '数据错误'
    #         })
    #     book_obj_list = []
    #     for i in pks:
    #         current_obj = Enterprise.objects.filter(pk=i, is_delete=False).first()
    #         if not current_obj:
    #             return Response({
    #                 'status': 1,
    #                 'msg': '数据错误'
    #             })
    #         book_obj_list.append(current_obj)
    #     book_der = EnterpriseSerializer(instance=book_obj_list, data=update_data, many=True, partial=True)
    #     print(type(book_der))
    #     book_der.is_valid(raise_exception=True)
    #     new_objs = book_der.save()
    #     return Response({
    #         'status': 0,
    #         'msg': 'ok',
    #         'results': EnterpriseSerializer(instance=new_objs, many=True).data
    #     })

    def delete(self, request, *args, **kwargs):
        """单删及群删"""
        pk = kwargs.get('pk')
        print('==delete PK==', pk)
        if pk:
            delete_obj = Enterprise.objects.filter(pk=pk, is_delete=False).update(is_delete=True)
        else:
            pks = request.data.get('pks')
            delete_obj = Enterprise.objects.filter(pk__in=pks, is_delete=False).update(is_delete=True)
        if delete_obj:
            return Response({
                'status': 0,
                'msg': '删除成功'
            })
        return Response({
            'status': 1,
            'msg': '删除失败'
        })
