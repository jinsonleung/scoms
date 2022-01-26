from django.urls import path
from apps.station import views

urlpatterns = [
    path('getall', views.get_all),
    path('add', views.add),
]

