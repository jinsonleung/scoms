from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ocr import views

urlpatterns = [
    path('temp', views.temp),   # for test
    path('accurateocr', views.accurate_ocr),    # 文字识别
]
