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


# 获取所有
@require_http_methods(['GET'])
def get_all(request):
    req = request.body
    response = {}
    all_queryset = Enterprise.objects.filter(is_delete=False)  # 获取所有人员列表（过滤软删除记录）
    print('==customers.count==', all_queryset)
    try:
        response['return_list'] = serializers.serialize('python', all_queryset, ensure_ascii=False)    # 对象序列化
        response['result_message'] = 'success'
        response['result_code'] = 0
    except Exception as e:
        response['result_message'] = str(e)
        response['result_code'] = 1
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
    total_counts = all_queryset.count()   # objects列表总记录数
    print('==total_counts==', total_counts)
    # total_pages = paginator.num_pages  # 一共多少页
    page_list = paginator.page(int(offset))  # 第int(offset)+1页
    page_list = EnterpriseSerializer(page_list, many=True).data  # 当前页上所有对象的列表
    try:
        response = {'result_message': 'success', 'result_body': page_list, 'result_code': 200, 'total_counts': total_counts}
    except Exception as e:
        response = {'result_message': 'failure', 'result_body': str(e), 'result_code': 40002}
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})    # 去除中文乱码


# 新增记录接口，方法一，POST
@require_http_methods(['POST'])
def add(request):
    """
    @func：新增记录接口，使用POST方式，要求前端传过来的日期格式为
    @param request：前端参数，格式为{data:'{*:*}',userName:*}
    @return: 是否成功对象
    """
    response = {}
    try:
        # 加载数据
        res = json.loads(request.body)
        data = res['data']
        # 判断企业账号是否存在（企业账号不可重复）
        is_exist = Enterprise.objects.filter(account=data['account']).exists()  # 查询所有记录并排序（过滤软删除记录）
        # 企业账号存在，则返回
        if is_exist:
            response = {'result_message': 'failure', 'result_body': 'account is existed', 'result_code': 40001}
            return JsonResponse(response)
        # 企业账号不存在，则保存
        enterprise = Enterprise(
            enterprise_level=data['enterpriseLevel'],
            account=data['account'],
            full_name=data['fullName'],
            abbreviation_name=data['abbreviationName'],
            enterprise_type=data['enterpriseType'],
            architecture=data['architecture'],
            unified_social_credit_code=data['unifiedSocialCreditCode'],
            registered_capital=data['registeredCapital'],
            established_date=data['establishedDate'] != '' and data['establishedDate'] or None,   # 类型不对
            effective_start_date=data['effectiveStartDate'] != '' and data['effectiveStartDate'] or None,
            effective_end_date=data['effectiveEndDate'] != '' and data['effectiveEndDate'] or None,
            address=data['address'],
            city=data['city'],
            industry=data['industry'],
            website=data['website'],
            legal_person_name=data['legalPersonName'],
            legal_person_email=data['legalPersonEmail'],
            contact_name=data['contactName'],
            contact_tel=data['contactTel'],
            contact_phone=data['contactPhone'],
            contact_email=data['contactEmail'],
            business_scope=data['businessScope'],
            remark=data['remark'],
            is_available=data['isAvailable'],
            # is_delete=data['']    # 默认不标删除标志
            # # create_datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            create_by=res['userName'],
            # # 格式化成2016-03-20 11:45:39形式
            # # update_datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            update_by=res['userName'],
        )
        enterprise.save()   # 保存
        # response['result_message'] = 'success'
        # response['result_code'] = 0
        response = {'result_message': 'success', 'result_body': '',  'result_code': 200}
    except Exception as e:
        response = {'result_message': 'failure', 'result_body': str(e), 'result_code': 40002}
    return JsonResponse(response)

# 删除记录接口，软删除
@require_http_methods(['POST'])
def delete(request):
    """
    @param request：前端参数，格式为{id:'deleteId'}
    @return: 是否成功对象
    """
    response = {}
    try:
        # 加载请求数据
        res = json.loads(request.body)
        # 进行软删除
        return_value = Enterprise.objects.filter(account=res['id']).update(is_delete=True)  # 更新记录
        if return_value == 1:
            response = {'result_message': 'success', 'result_body': 'one record is deleted',  'result_code': 200}
        else:
            response = {'result_message': 'failure', 'result_body': '',  'result_code': 40003}
    except Exception as e:
        response = {'result_message': 'failure', 'result_body': str(e), 'result_code': 40004}
    return JsonResponse(response)


# 查询记录接口
@require_http_methods(['POST'])
def search(request):
    """
    @param request：前端参数，格式为{id:***}或{fuzzy_full_name:***}
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

