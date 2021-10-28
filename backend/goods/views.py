from goods.models import Goods
from django.http import JsonResponse


def addNewGoods(request):
    print('==request.FILES==', request.FILES)
    response = {}
    goods_title = request.POST.get('goods_title')
    goods_price = request.POST.get('goods_price')
    goods_image = request.FILES.get('goods_image')
    goods_kind = request.POST.get('goods_kind')
    goods_obj = Goods.objects.create(goods_title=goods_title, goods_price=goods_price, goods_image=goods_image, goods_kind=goods_kind)
    goods_obj.save()
    response['msg'] = '添加成功'
    response['error_num'] = 0
    return JsonResponse(response)
