# from django.contrib import admin
# from django.urls import path, include, re_path
#
# from apps.enterprise import views
# from backend.settings import MEDIA_ROOT
# from django.views.static import serve


# urlpatterns = [
#     re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
#     # path('admin/', admin.site.urls),
#     # path('books/', include('books.urls')),    # url: books/xxx
#     # path('ocr/', include('ocr.urls')),    # url: ocr/xxx，文字识别接口
#     # path('station/', include('station.urls')),    # url: station/xxx，场站信息接口
#     # path('goods/', include('goods.urls')),    # url: goods/xxx，场站信息接口
#     # path('customer/', include('customer.urls')),  # url: customer/xxx
#     # path('enterprise/', include('enterprise.urls')),  # 企业信息，url: enterprise-1/xxx
#     path(r'enterprise/$', views.Enterprise.as_view()),
#
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.test0130 import views

# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'news', views.NewsViewSet)
#
# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    # path('', include('test0130.urls')),
    path('', include('enterprise.urls')),
]

