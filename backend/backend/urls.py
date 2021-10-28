"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

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
