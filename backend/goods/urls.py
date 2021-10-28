from django.urls import path, include
from goods import views

urlpatterns = [
    path('addNewGoods', views.addNewGoods),
]

