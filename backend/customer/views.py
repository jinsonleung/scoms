from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets, serializers
from customer.models import Customer
from customer.serializer import CustomerSerializer
from django.core import serializers
import json


# 图书类视图集
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# 获取所有
@require_http_methods(['GET'])
def get_all(request):
    req = request.body
    print("==request.body==", req)
    response = {}
    customers = Customer.objects.filter()  # 获取所有人员列表
    print('==customers.count==', customers)
    try:
        # customers = Customer.objects.filter()   # 获取所有人员列表
        # customers = Customer.objects.values('registration_date').first()   # 获取所有人员列表
        print('==customers==', customers)
        response['list'] = serializers.serialize('python', customers, ensure_ascii=False)    # 对象序列化
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})    # 去除中文乱码

