from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets, serializers
from demo.books.models import Books
from demo.books.serializer import BooksSerializer
from django.core import serializers
import json


# 图书类视图集
class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


# 获取所有
@require_http_methods(['GET'])
def get_all(request):
    req = request.body
    print("==request.body==", req)
    response = {}
    try:
        persons = Books.objects.filter()   # 获取所有人员列表
        response['list'] = serializers.serialize('python', persons, ensure_ascii=False)    # 对象序列化
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})    # 去除中文乱码


# 新增记录接口，方法一,GET
@require_http_methods(['GET'])
def add(request):
    response = {}
    try:
        book = Books(
            name=request.GET.get('name'),
            author=request.GET.get('author')
        )
        book.save()   # 保存
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 新增记录接口，方法一，POST
@require_http_methods(['POST'])
def add_book(request):
    response = {}
    try:
        res = json.loads(request.body)  # 加载数据
        print('rest====', res)
        print('name:', res['name'])
        book = Books(
            name=res['name'],
            author=res['author']
        )
        book.save()   # 保存
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response = {'error', str(e)}
    return JsonResponse(response)


# 新增记录接口，方法二，POST
@require_http_methods(['POST'])
def add_book_2(request):
    response = {}
    try:
        res = json.loads(request.body)  # 加载数据
        print('rest====', res)
        print('name:', res['name'])
        book = Books(
            name='环球地理杂志1',
            author='Peter.Yon1'
        )
        book.save()   # 保存
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response = {'error', str(e)}
    return JsonResponse(response)
