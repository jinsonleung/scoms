import random
import base64
from apps.goods.models import Goods
from django.http import JsonResponse
import os
import time
from django.conf import settings
import requests

def add_new_goods(request):
    print('==request.FILES==', request.FILES)
    response = {}
    goods_title = request.POST.get('goods_title')
    goods_price = request.POST.get('goods_price')
    goods_image = request.FILES.get('goods_image')
    # print("==goods_image==", goods_image)
    goods_kind = request.POST.get('goods_kind')
    goods_obj = Goods.objects.create(goods_title=goods_title, goods_price=goods_price, goods_image=goods_image, goods_kind=goods_kind)
    goods_obj.save()
    response['msg'] = '添加成功'
    response['error_num'] = 0
    return JsonResponse(response)


"""
保存前端上传的图片（其他）文件
"""
def save_file(request):
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
    ocr_old(img_path)
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










