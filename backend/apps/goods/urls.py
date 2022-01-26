from django.urls import path
from apps.goods import views

urlpatterns = [
    path('addNewGoods', views.add_new_goods),
    path('savefile', views.save_file),
]

