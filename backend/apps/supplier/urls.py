from django.template.defaulttags import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.supplier import views

# """
# @func：接口URL
# """


# urlpatterns = [
#     path('supplier/', views.SupplierList.as_view()),
#     path('supplier/<int:pk>', views.SupplierDetail.as_view()),
#
#
#     ]
# urlpatterns = format_suffix_patterns(urlpatterns)

from rest_framework.routers import SimpleRouter
from django.views.static import serve
from django.conf import settings
from django.urls import re_path

# 1.创建SimpleRouter实例对象
router = SimpleRouter()
# 2.注册路由
router.register('supplier', views.SupplierModelViewSet, basename='supplier')

urlpatterns = [
    # url(r'media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]

# 3.挂载到urlpatters
urlpatterns += router.urls
