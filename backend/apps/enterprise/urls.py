from django.urls import path, include
from apps.enterprise import views

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
    # 修改记录接口： enterprise/update
    path('update', views.update),
    # 删除记录接口： enterprise/delete，软删除
    path('delete', views.delete),
    # 查找记录接品：enterprise/search
    path('search', views.search),
    ]



