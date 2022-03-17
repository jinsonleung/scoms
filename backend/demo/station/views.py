from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets, serializers
from demo.station.models import Station
from demo.station.serializer import StationSerializer
from django.core import serializers
import json


# 图书类视图集
class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


# 获取所有
@require_http_methods(['GET'])
def get_all(request):
    req = request.body
    print("==request.body==", req)
    response = {}
    try:
        stations = Station.objects.filter()   # 获取所有人员列表
        response['list'] = serializers.serialize('python', stations, ensure_ascii=False)    # 对象序列化
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})    # 去除中文乱码


# 新增记录接口，方法二，POST
@require_http_methods(['POST'])
def add(request):
    response = {}
    try:
        res = json.loads(request.body)  # 加载数据
        print('rest====', res)
        print('station_code:', res['station_code'])
        station = Station(
            station_code=res['station_code'],
            station_name=res['station_name'],
            station_address=res['station_address'],
            facility_code=res['facility_code'],
            employees=res['employees'],
            update_datetime=res['update_datetime'],
            is_delete=False,
            create_user=res['create_user'],
        )
        station.save()   # 保存
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response = {'error', str(e)}
    return JsonResponse(response)




