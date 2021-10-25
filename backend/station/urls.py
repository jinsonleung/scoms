from django.urls import path, include
from rest_framework.routers import DefaultRouter
from station import views

urlpatterns = [
    path('getall', views.get_all),
    path('add', views.add),
]

