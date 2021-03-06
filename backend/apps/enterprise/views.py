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
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """单增及群增"""
        try:
            json_data = {"result_msg": "ok", "result_code": 0, "result_data": ""}
            request_data = request.data
            if isinstance(request_data, dict):
                many = False
                if Enterprise.custom.filter(account=request_data['account']).first():
                    # render.ret.result_msg='aaa'
                    return JsonResponse({"result_msg": "failure", "result_code": 401, "result_data": '重复账号'})
            elif isinstance(request_data, list):
                many = True
            else:
                raise exceptions.ValidationError('数据格式不正确')
            Enterprise.custom.get_or_create(account=request_data['account'])

            obj_serial = EnterpriseSerializer(data=request_data, many=many)
            obj_serial.is_valid(raise_exception=True)
            # obj_serial.is_valid()
            obj_result = obj_serial.save()
            # 获取序列化数据
            obj_data = EnterpriseSerializer(instance=obj_result, many=many).data
            return JsonResponse(obj_data)
        except Exception as e:
            print('发生错误：', e)
            return Response({"error_msg": "出现了无法预料的view视图错误：%s" % e, "error_code": 1, "error_data": {}})


class EnterpriseDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    """获取、更新或删除一条记录"""
    # queryset = Enterprise.objects.all()   # 获取所有记录
    queryset = Enterprise.custom.all()  # 获取非软删除的记录
    serializer_class = EnterpriseSerializer

    def get(self, request, *args, **kwargs):
        """单查"""
        print('==单查==', kwargs.get('pk'))
        return self.retrieve(request, *args, **kwargs)

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
