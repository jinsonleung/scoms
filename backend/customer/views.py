from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets, serializers
from customer.models import Customer
from customer.serializer import CustomerSerializer
from django.core import serializers
import json
#分页器Paginator,是导入了一个类，在用实列出来的对象调用方法，
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from customer.serializer import CustomerSerializer


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


# 获取分页列表，正确
@require_http_methods(['GET'])
def get_page_list(request):
    response = {}
    limit = request.GET.get('limit')    # 页长，获取get url(customer/getpagelist?limit=10&offset=0)参数
    offset = request.GET.get('offset')    # 偏移量，获取get url(customer/getpagelist?limit=10&offset=0)参数
    customer_queryset = Customer.objects.all().order_by('company_account')  # 查询所有记录并排序
    # customer_queryset = customer_queryset.order_by('company_name')
    paginator = Paginator(customer_queryset, limit)  # 获取Paginator对象,将customers列表分为每页limit条数据
    total_counts = paginator.count   # objects列表总记录数
    # total_pages = paginator.num_pages  # 一共多少页
    customer_list = paginator.page(int(offset)+1)  # 第int(offset)+1页
    customer_list = CustomerSerializer(customer_list, many=True).data  # 当前页上所有对象的列表
    try:
        # response['customerList'] = serializers.serialize('python', page_object_list, ensure_ascii=False)  # 对象序列化
        response['customerList'] = customer_list  # 对象序列化
        response['length'] = total_counts
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})    # 去除中文乱码
