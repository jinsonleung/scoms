# encoding:utf-8
import requests
import base64
import os
import time
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from django.conf import settings
import random

# 获取所有
@require_http_methods(['GET'])
def temp(request):
    print("==request.body==", request.body)
    response = {
        'code': '200',
        'msg': 'accurate ocr success',
        # 'img_url': img_url
    }
    return JsonResponse(response)


@require_http_methods(['POST'])
def accurate_ocr(request):
    print('==收到数据啦,request.body==', request.body)
    # file_img = request.data.get('files', None)
    file_img = request.data.get('file', None)
    print("==file_img==", file_img)
    response = {
        'code': '200',
        'msg': 'accurate ocr success',
        # 'img_url': img_url
    }
    return JsonResponse(response)
    # if response:
    #     print(response.json())


@require_http_methods(['POST'])
def accurate_ocr_1(request):   # 正确，但还没存放图片
    print('==收到数据啦==', request)
    # file_name = request.POST.get('fileList')
    res = json.loads(request.body)  # 加载数据
    file_name = res['img_url']
    # file_name = request.body
    print('==文件名是==', file_name)

    # request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # # f = open(r'D:\Temp\14_Sep_2021_QF_CN38_01.jpg', 'rb')
    # res = json.loads(request.body)  # 加载数据
    # img_url = res['img_url']    # 获取图片url
    # print("==img_url==", img_url)
    # f = open(img_url)   # 找不到前文件
    # img = base64.b64encode(f.read())
    # params = {"image": img}
    # # access_token = '[调用鉴权接口获取的token]'
    # access_token = '24.b5662b1792c615791f371ff9bb69ac16.2592000.1634450445.282335-24861375'
    # request_url = request_url + "?access_token=" + access_token
    # headers = {'content-type': 'application/x-www-form-urlencoded'}
    # response = requests.post(request_url, data=params, headers=headers)
    response = {
        'code': '200',
        'msg': 'accurate ocr success',
        # 'img_url': img_url
    }
    return JsonResponse(response)
    # if response:
    #     print(response.json())


# for test
@require_http_methods(['POST'])
def addNewGoods(request):
    print("==addNewGoods==", request.FILES)
    goods_image = request.FILES.get('goods_image')
    print("==goods_image==", goods_image)

    goods_title = request.POST.get('goods_title')
    goods_price = request.POST.get('goods_price')
    goods_kind = request.POST.get('goods_kind')
    # goods_id = str(time.time()).replace('.', '')
    #
    # goods_obj = GoodsList.objects.create(goods_id=goods_id, goods_title=goods_title, goods_price=goods_price,
    #                                      goods_kind=goods_kind, goods_image=goods_image, goods_order_num=0)
    # goods_obj.save()
    #
    # data = jsonResult.json_result(message="添加成功", result="success", data=[], form_data={})

    response = {
        'code': '200',
        'msg': 'accurate ocr success',
        # 'img_url': img_url
    }
    return JsonResponse(response)


# =============================2021.11.03更新 开始==================================

"""
功能:获取baidu api的token，baidu api官网一个月更新一次
结果:正确 
"""
def get_access_token(request):
    response = {}
    client_id = 'NfKHZmftHaYidIoGspW6F3hQ'  # client_id 为官网获取的AK
    client_secret = '5VO7xubpj7m5uOrq7xa8NjAFX4QloZ3g'  # client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
    response = requests.get(host)
    if response:
        result = response.json()
        access_token = result["access_token"]
        response = {
            'code': '200',
            'msg': 'get baidu ocr access_token successfully',
            'access_token': access_token,
        }
    return JsonResponse(response)


def save_file_old(request):
    response = {}
    img = request.FILES.get('goods_image')  # 获取上传的图片
    date_str = time.strftime('%Y%m%d', time.localtime(time.time()))  # 年月日格式，如20210823
    datetime_str = time.strftime('%y%m%d%H%M%S', time.localtime(time.time()))  # 年月日格式时间,如210823104552
    img_ext = os.path.splitext(img.name)[1]  # 取图片文件扩展名,如".jpg“
    img_name = 'Img' + datetime_str + str(random.randint(10, 100)) + img_ext   # 拼接图片文件名，文件名='Img'+年(2位)月日格式时间+两位随机整数+'.'+后缀,如Img21110314000277.jpg
    img_path_dir = os.path.join(settings.IMG_UPLOAD + '/' + date_str)   # 文件目录
    if not os.path.exists(img_path_dir):    # 判断文件目录是否存在，若不存在则创建
        os.makedirs(img_path_dir)   # 创建文件目录
    img_path = os.path.join(img_path_dir, img_name)  # 拼接图片存放路径
    with open(img_path, 'ab') as fp:
        for chunk in img.chunks():  # 如果上传的图片非常大， 那么通过 img对象的 chunks() 方法 分割成多个片段来上传
            fp.write(chunk)
    ocr(img_path)
    response['msg'] = '添加成功'
    response['error_num'] = 0
    return JsonResponse(response)

"""
图片文字识别
"""
def ocr_old(file_path):
    print("===ocr===", file_path)
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    f = open(file_path, 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img}
    # access_token = '[调用鉴权接口获取的token]'
    access_token = '24.ffc04550c78b415a3940baae92f05e04.2592000.1638514710.282335-24861375'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print('==response.json()==', response.json())
    return JsonResponse(response)


def save_file(file_abs_path):
    response = {}
    file_folder = os.path.dirname(file_abs_path)
    file_name = os.path.split(file_abs_path)[-1]
    print('file_folder===', file_folder)
    print('file_name===', file_name)
    response['msg'] = '添加成功'
    response['error_num'] = 0
    return JsonResponse(response)

"""
图片文字识别
"""
def ocr(request):
    response = {}
    img = request.FILES.get('goods_image')  # 获取上传的图片
    date_str = time.strftime('%Y%m%d', time.localtime(time.time()))  # 年月日格式，如20210823
    datetime_str = time.strftime('%y%m%d%H%M%S', time.localtime(time.time()))  # 年月日格式时间,如210823104552
    img_ext = os.path.splitext(img.name)[1]  # 取图片文件扩展名,如".jpg“
    img_name = 'Img' + datetime_str + str(random.randint(10, 100)) + img_ext   # 拼接图片文件名，文件名='Img'+年(2位)月日格式时间+两位随机整数+'.'+后缀,如Img21110314000277.jpg
    img_path_dir = os.path.join(settings.IMG_UPLOAD + '/' + date_str)   # 文件目录
    img_abs_path = os.path.join(img_path_dir, img_name)  # 拼接图片存放路径

    save_file(img_abs_path)


    return JsonResponse(response)

# =============================2021.11.03更新 结束==================================






