from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets, serializers
from enterprise.models import Enterprise

from django.core import serializers
import json
# 分页器Paginator,是导入了一个类，在用实列出来的对象调用方法，
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from enterprise.serializer import EnterpriseSerializer


# 获取所有
@require_http_methods(['GET'])
def get_all(request):
    req = request.body
    response = {}
    all_queryset = Enterprise.objects.filter(is_delete=False)  # 获取所有人员列表（过滤软删除记录）
    print('==customers.count==', all_queryset)
    try:
        response['return_list'] = serializers.serialize('python', all_queryset, ensure_ascii=False)    # 对象序列化
        response['return_message'] = 'success'
        response['error_number'] = 0
    except Exception as e:
        response['return_message'] = str(e)
        response['error_number'] = 1
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})    # 去除中文乱码


# 功能：获取分页列表，正确
# 参数：url?limit=10&offset=0，如customer/getpagelist?limit=10&offset=0
# 返回：分面数据
@require_http_methods(['GET'])
def get_page_list(request):
    response = {}   # 返回值对象
    limit = request.GET.get('limit')    # 页长，获取get url(enterprise/getpagelist?limit=10&offset=0)参数
    offset = request.GET.get('offset')    # 偏移量，获取get url(enterprise/getpagelist?limit=10&offset=0)参数
    # all_queryset = Enterprise.objects.all().order_by('account')  # 查询所有记录并排序
    all_queryset = Enterprise.objects.filter(is_delete=False).order_by('account')  # 查询所有记录并排序（过滤软删除记录）
    paginator = Paginator(all_queryset, limit)  # 获取Paginator对象,将customers列表分为每页limit条数据
    total_counts = paginator.count   # objects列表总记录数
    # total_pages = paginator.num_pages  # 一共多少页
    page_list = paginator.page(int(offset)+1)  # 第int(offset)+1页
    page_list = EnterpriseSerializer(page_list, many=True).data  # 当前页上所有对象的列表
    try:
        response['return_list'] = page_list  # 对象序列化
        response['total_counts'] = total_counts
        response['return_message'] = 'success'
        response['error_number'] = 0
    except Exception as e:
        response['return_message'] = str(e)
        response['error_number'] = 1
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})    # 去除中文乱码
