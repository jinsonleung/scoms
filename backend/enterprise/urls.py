from django.urls import path, include
from rest_framework.routers import DefaultRouter
from enterprise import views

"""
@func：企业记录接口
"""
urlpatterns = [
    # 获取全部记录接口：enterprise/getall
    path('getall', views.get_all),
    # 获取分页记录接口： enterprise/getpagelist?limit=10&offset=0
    path('getpagelist', views.get_page_list),
    # 新增记录接口： enterprise/add
    path('add', views.add),
    ]



