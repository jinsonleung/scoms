import requests
import base64
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json


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
