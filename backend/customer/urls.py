from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customer import views


urlpatterns = [
    path('getall', views.get_all),
    # path('add', views.add),
    # path('addbook', views.add_book),
    # path('addbook2', views.add_book_2),
]

