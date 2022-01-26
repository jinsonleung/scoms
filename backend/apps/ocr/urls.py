from django.urls import path
from apps.ocr import views

urlpatterns = [
    path('temp', views.temp),   # for test
    path('accurateocr', views.accurate_ocr),    # 文字识别
    path('addNewGoods', views.addNewGoods),
    path('getaccesstoken', views.get_access_token),  # 获取 baidu api的token
    path('accurateocr', views.accurate_ocr),  # 获取 baidu api的token


]

