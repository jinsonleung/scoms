import pickle

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets, serializers
from apps.enterprise.models import Enterprise
from django.core import serializers
import json
import time
# 分页器Paginator,是导入了一个类，在用实列出来的对象调用方法，
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.enterprise.serializer import EnterpriseSerializer
from rest_framework.response import Response


# 获取所有，使用GET请求
@require_http_methods(['GET'])
def get_all(request):
    '''
    @func：获取所有记录()，使用GET请求
    @param：null
    @return：所有记录
    '''
    try:
        enterprises = Enterprise.custom.all()
        enterprises = serializers.serialize('python', enterprises, ensure_ascii=False)  # 对象序列化
        response = {'result_message': 'success', 'result_body': enterprises, 'result_code': 200}
    except Exception as e:
        response = {'result_message': 'failure', 'result_body': str(e), 'result_code': 5001}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})  # 去除中文乱码


@require_http_methods(['GET'])
def get_page_list(request):
    '''
    @func：获取分页列表，使用GET请求，正确
    @param request：url?limit=10&offset=0，如：enterprise/getpagelist?limit=10&offset=0
    @return：分页数据
    '''
    try:
        limit = request.GET.get('limit')  # 页长，获取get url(enterprise/getpagelist?limit=10&offset=0)参数
        offset = request.GET.get('offset')  # 偏移量，获取get url(enterprise/getpagelist?limit=10&offset=0)参数
        enterprises = Enterprise.custom.all()
        paginator = Paginator(enterprises, limit)  # 获取Paginator对象,将customers列表分为每页limit条数据
        total_counts = enterprises.count()  # objects列表总记录数
        print('==total_counts==', total_counts)
        # total_pages = paginator.num_pages  # 一共多少页
        page_list = paginator.page(int(offset))  # 第int(offset)+1页
        page_list = EnterpriseSerializer(page_list, many=True).data  # 当前页上所有对象的列表
        response = {'result_message': 'success', 'result_body': page_list, 'result_code': 200, 'total_counts': total_counts}
    except Exception as e:
        response = {'result_message': 'failure', 'result_body': str(e), 'result_code': 40002}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})  # 去除中文乱码


@require_http_methods(['POST'])
def add(request):
    """
    @func：增加记录接口，使用POST方式，要求前端传过来的日期格式为
    @param request：前端参数，如enterprise/{data:'{*:*}',userName:*}
    @return: 是否成功对象
    """
    try:
        # 将前端传过来的json格式数据转换为字典
        res = json.loads(request.body)
        data = res['data']
        user_name = res['user_name']
        # 判断企业账号是否存在（企业账号不可重复）
        is_exist = Enterprise.objects.filter(account=data['account']).exists()  # 查询所有记录并排序
        # 企业账号存在，则返回
        if is_exist:
            response = {'result_message': 'failure', 'result_body': 'account is existed', 'result_code': 40001}
            return JsonResponse(response)
        # 若前端的日期字段为空，则将从字典中移除，否则执行save()方法时报错
        if data['established_date'] == '': del data['established_date']
        if data['effective_start_date'] == '': del data['effective_start_date']
        if data['effective_end_date'] == '': del data['effective_end_date']
        # 将字典转为对象,参考https://www.jb51.net/article/163765.htm
        enterprise = Enterprise(create_by=user_name, update_by=user_name, **data)
        enterprise.save()
        response = {'result_message': 'success', 'result_body': 'save is successful', 'result_code': 200}
        return JsonResponse(response)
    except Exception as e:
        response = {'result_message': 'failure', 'result_body': str(e), 'result_code': 50002}
    return JsonResponse(response)


@require_http_methods(['POST'])
def add_old(request):
    """
    @func：增加记录接口，使用POST方式，要求前端传过来的日期格式为
    @param request：前端参数，如enterprise/{data:'{*:*}',userName:*}
    @return: 是否成功对象
    """
    response = {}
    try:
        # 加载数据
        res = json.loads(request.body)
        data = res['data']
        # 判断企业账号是否存在（企业账号不可重复）
        is_exist = Enterprise.objects.filter(account=data['account']).exists()  # 查询所有记录并排序
        # 企业账号存在，则返回
        if is_exist:
            response = {'result_message': 'failure', 'result_body': 'account is existed', 'result_code': 40001}
            return JsonResponse(response)
        # 企业账号不存在，则保存
        enterprise = Enterprise(
            superior_level=data['superior_level'],
            account=data['account'],
            full_name=data['full_name'],
            abbreviation_name=data['abbreviation_name'],
            enterprise_type=data['enterprise_type'],
            architecture=data['architecture'],
            unified_social_credit_code=data['unified_social_credit_code'],
            registered_capital=data['registered_capital'],
            established_date=data['established_date'] != '' and data['established_date'] or None,  # 类型不对
            effective_start_date=data['effective_start_date'] != '' and data['effective_start_date'] or None,
            effective_end_date=data['effective_end_date'] != '' and data['effective_end_date'] or None,
            address=data['address'],
            city=data['city'],
            industry=data['industry'],
            website=data['website'],
            legal_person_name=data['legal_person_name'],
            legal_person_email=data['legal_person_email'],
            contact_name=data['contact_name'],
            contact_tel=data['contact_tel'],
            contact_phone=data['contact_phone'],
            contact_email=data['contact_email'],
            business_scope=data['business_scope'],
            remark=data['remark'],
            is_available=data['is_available'],
            # is_delete=data['']    # 默认不标删除标志
            # # create_datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            create_by='admin',    #res['create_by'],
            # # 格式化成2016-03-20 11:45:39形式
            # # update_datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            update_by='admin',    #res['update_by'],
        )
        print('==enterprise==', enterprise)
        enterprise.save()  # 保存
        # response['result_message'] = 'success'
        # response['result_code'] = 0
        response = {'result_message': 'success', 'result_body': '', 'result_code': 200}
    except Exception as e:
        response = {'result_message': 'failure', 'result_body': str(e), 'result_code': 40002}
    return JsonResponse(response)


@require_http_methods(['POST'])
def update(request):
    res0 = request.body
    res1 = json.loads(request.body)
    # res2 = EnterpriseSerializer(request.body)
    data1 = res1['data']
    # data2 = res2['data']

    data2 = EnterpriseSerializer(data=data1)

    print('==res0==', res0)
    print('==data1==', data1)
    print('==data2==', data2)
    # print('==data2.account==', data2['account'])
    response = {'result_message': '222', 'result_body': 'update is successful', 'result_code': 222}
    if data2.is_valid():
        data2.save()
        response = {'result_message': 'failure', 'result_body': 'account is not existed', 'result_code': 40001}
        return JsonResponse(response)
    return JsonResponse(response)

@require_http_methods(['POST'])
def update_old(request):
    """
    @func：根据account修改记录接口，使用POST方式，参数格式为{data:'{*:*}',userName:*}
    @param request：前端参数，如enterprise/{data:'{*:*}',userName:*}
    @return: 是否成功对象
    """
    # try:
    # 将前端传过来的json格式数据转换为字典
    res = json.loads(request.body)
    data = res['data']
    print('==data==', data)

    user_name = res['user_name']
    # 判断企业账号是否存在（企业账号不可重复）
    is_exist = Enterprise.objects.filter(account=data['account']).exists()
    # enterprise = Enterprise.custom.filter(account=data['account']).first()
    print('==is_exist==', is_exist)
    # 记录不存在，则返回
    if is_exist is False:
        response = {'result_message': 'failure', 'result_body': 'account is not existed', 'result_code': 40001}
        return JsonResponse(response)
    # 若前端的日期字段为空，则将从字典中移除，否则执行save()方法时报错
    if data['established_date'] == '': del data['established_date']
    if data['effective_start_date'] == '': del data['effective_start_date']
    if data['effective_end_date'] == '': del data['effective_end_date']
    # del data['create_datetime']
    # 将字典转为对象,参考https://www.jb51.net/article/163765.htm
    enterprise = Enterprise(update_by=user_name, **data)
    enterprise.save()
    response = {'result_message': 'success', 'result_body': 'update is successful', 'result_code': 200}
    return JsonResponse(response)
    # except Exception as e:
    #     response = {'result_message': 'failure', 'result_body': str(e), 'result_code': 50002}
    # return JsonResponse(response)


@require_http_methods(['POST'])
def delete(request):
    """
    @func：删除记录（软删除）
    @param request：前端参数，格式为{id:'deleteId'}
    @return: 是否成功对象
    """
    try:
        # 加载请求数据
        res = json.loads(request.body)
        # 进行软删除
        return_value = Enterprise.objects.filter(account=res['id']).update(is_delete=True)  # 更新记录
        if return_value == 1:
            response = {'result_message': 'success', 'result_body': 'one record is deleted', 'result_code': 200}
        else:
            response = {'result_message': 'failure', 'result_body': '', 'result_code': 40003}
    except Exception as e:
        response = {'result_message': 'failure', 'result_body': str(e), 'result_code': 40004}
    return JsonResponse(response)


@require_http_methods(['GET'])
def search(request):
    """
    @func：根据查询条件查询记录（支持模糊查询）
    @param request：前端参数，格式为{id:***}或{fuzzy_name:‘模糊查询内容’}
    @return: 是否成功对象
    """
    response = {}
    # try:
    #     # 加载请求数据
    #     res = json.loads(request.body)
    #     account = res['account']
    #     fuzzy_full_name = res['fuzzy_name']

    # query_set = account == '' and Enterprise.objects.filter(is_delete=false and account=account) # or Enterprise.objects.filter(full_name__contains=fuzzy_full_name)

    # query_set = Enterprise.objects.filter(is_delete=false && account = account)
    #
    #
    # if query_set.count() > 0:
    #     total_counts = query_set.count()    # objects列表总记录数
    #     print('==total_counts==', total_counts)
    #     page_list = paginator.page(int(offset))  # 第int(offset)+1页
    #     page_list = EnterpriseSerializer(page_list, many=True).data  # 当前页上所有对象的列表
    #     try:
    #         response = {'result_message': 'success', 'result_body': page_list, 'result_code': 200, 'total_counts': total_counts}
    #     except Exception as e:
    #         response = {'result_message': 'failure', 'result_body': str(e), 'result_code': 40002}
    #     return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})
