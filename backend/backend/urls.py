from django.urls import path, include

urlpatterns = [
    path('', include('enterprise.urls')),   # 报错
]

