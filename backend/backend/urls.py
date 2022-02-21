from django.urls import path, include

urlpatterns = [
    path('', include('enterprise.urls')),   # 企业信息
    path('', include('universalCode.urls')),   # 机场信息

]

