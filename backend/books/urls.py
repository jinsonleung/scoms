from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books import views

# router = DefaultRouter()
# router.register('books', views.BooksViewSet)
#
# urlpatterns = [
#     path('aa', include(router.urls))   # 查询所有
# ]


urlpatterns = [
    path('getall', views.get_all),
    path('add', views.add),
    path('addbook', views.add_book),
]

