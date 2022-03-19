from django.urls import path, include

urlpatterns = [
    path('', include('enterprise.urls')),   # 企业信息
    path('', include('universalCode.urls')),   # 机场信息
    path('', include('supplier.urls')),   # 供应商信息
    # 以下urls用于测试
    # path('demo/', include('demo.student.urls')),
    path('demo/', include('demo.school.urls')),
]

