from django.urls import path, include
from rest_framework.routers import DefaultRouter
from enterprise import views


urlpatterns = [
    path('getall', views.get_all),  # 接口：enterprise/getall
    path('getpagelist', views.get_page_list),  # 接口： enterprise/getpagelist?limit=10&offset=0
    ]



