from django.db.models import Q
from django.http import JsonResponse
from rest_framework.response import Response
from utils.pagination import Pagination
from apps.freightTools.airport11.models import Airport
from apps.freightTools.airport11.serializers import AirportSerializer
from rest_framework import mixins, exceptions
from rest_framework import generics


class AirportList(generics.ListAPIView, mixins.CreateModelMixin, generics.GenericAPIView):
    """列出所有的记录，或创建一条新的记录"""
    # queryset = Airport.objects.all()   # 获取所有记录
    queryset = Airport.custom.all()  # 获取非软删、除的记录
    serializer_class = AirportSerializer  # 序列化
    pagination_class = Pagination  # 分页

    def get(self, request, *args, **kwargs):
        query_text = request.query_params.get('query')
        if query_text != '':
            query_text = query_text.upper()
            print('==查询开始==', query_text)
            # 查询条件Q组合,模糊查询
            query_criteria = Q(iata_code__contains=query_text) | Q(icao_code__contains=query_text) | Q(airport_chn_name__contains=query_text) | Q(country_chn_name__contains=query_text) | Q(city_chn_name__contains=query_text)
            query_result = Airport.custom.filter(query_criteria)
            page = self.paginate_queryset(query_result)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(query_result, many=True)
            return Response(serializer.data)
        return self.list(request, *args, **kwargs)



    def get_0(self, request, *args, **kwargs):
        """群查，获取分页数据"""
        # 获取url中的需要查询的内容
        print('==request.query_params==', request.query_params.dict())
        # query_text = request.query_params.get('query')
        # if query_text == '':
        #     print('==查询开始==', '*' + query_text + '*')
        # # if (query_text):
        # return JsonResponse({'a':'aaa'})
        query_text = request.query_params.get('query')
        if query_text != '':
            query_text = query_text.upper()
            print('==查询开始==', query_text)
            query_result = Airport.custom.filter(Q(iata_code__contains=query_text) | Q(icao_code__contains=query_text) | Q(airport_chn_name__contains=query_text) | Q(country_chn_name__contains=query_text) | Q(city_chn_name__contains=query_text))
            # print('==query_result==', query_result)
            # obj_data = AirportSerializer(instance=query_result, many=True).data
            # pg_data = Pagination.paginate_queryset(queryset=query_result, request=request, view=self)
            # pg_data = Pagination.paginate_queryset(self, queryset=query_result, request=request, view=None)
            # pg_data = self.paginate_queryset(query_result)
            # obj_data = AirportSerializer(instance=pg_data, many=True).data
            obj_data = AirportSerializer(instance=query_result, many=True).data
            return Response(obj_data)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """单增及群增"""
        try:
            json_data = {"result_msg": "ok", "result_code": 0, "result_data": ""}
            request_data = request.data
            if isinstance(request_data, dict):
                many = False
                if Airport.custom.filter(iata_code=request_data['iata_code']).first():
                    # render.ret.result_msg='aaa'
                    return JsonResponse({"result_msg": "failure", "result_code": 401, "result_data": '重复账号'})
            elif isinstance(request_data, list):
                many = True
            else:
                raise exceptions.ValidationError('数据格式不正确')
            Airport.custom.get_or_create(iata_code=request_data['iata_code'])

            obj_serial = AirportSerializer(data=request_data, many=many)
            obj_serial.is_valid(raise_exception=True)
            # obj_serial.is_valid()
            obj_result = obj_serial.save()
            # 获取序列化数据
            obj_data = AirportSerializer(instance=obj_result, many=many).data
            return JsonResponse(obj_data)
        except Exception as e:
            print('发生错误：', e)
            return Response({"error_msg": "出现了无法预料的view视图错误：%s" % e, "error_code": 1, "error_data": {}})


class AirportDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    """获取、更新或删除一条记录"""
    # queryset = Airport.objects.all()   # 获取所有记录
    queryset = Airport.custom.all()  # 获取非软删除的记录
    serializer_class = AirportSerializer

    def get(self, request, *args, **kwargs):
        """单查"""
        print('==单查==', **kwargs)
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """提供全部数据，单改"""
        request_data = request.data
        pk = kwargs.get('pk')
        print('==put PK==', pk)
        try:
            current_obj = Airport.objects.filter(pk=pk, is_delete=False).first()
            if not current_obj:
                raise exceptions.ValidationError('数据错误')
        except:
            return Response({
                'status': 1,
                'msg': '数据错误'
            })
        # 需要进行update时,要同时传入instance和data
        obj_serial = AirportSerializer(instance=current_obj, data=request_data)
        obj_serial.is_valid(raise_exception=True)
        new_obj = obj_serial.save()
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': AirportSerializer(instance=new_obj).data
        })

    def delete(self, request, *args, **kwargs):
        """单删及群删"""
        pk = kwargs.get('pk')
        print('==delete PK==', pk)
        if pk:
            delete_obj = Airport.objects.filter(pk=pk, is_delete=False).update(is_delete=True)
        else:
            pks = request.data.get('pks')
            delete_obj = Airport.objects.filter(pk__in=pks, is_delete=False).update(is_delete=True)
        if delete_obj:
            return Response({
                'status': 0,
                'msg': '删除成功'
            })
        return Response({
            'status': 1,
            'msg': '删除失败'
        })
