from django.contrib import admin
from django.urls import path, include, re_path
from backend.settings import MEDIA_ROOT
from django.views.static import serve


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),    # url: books/xxx
    path('ocr/', include('ocr.urls')),    # url: ocr/xxx，文字识别接口
    path('station/', include('station.urls')),    # url: station/xxx，场站信息接口
    path('goods/', include('goods.urls')),    # url: goods/xxx，场站信息接口

]
