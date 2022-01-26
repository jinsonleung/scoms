from django.urls import path
from apps.books import views

# router = DefaultRouter()
# router.register('books', views.BooksViewSet)
#
# urlpatterns = [
#     path('aa', include(router.urls))   # 查询所有
# ]


urlpatterns = [
    path('getall', views.get_all),
    # path('add', views.add),
    # path('addbook', views.add_book),
    # path('addbook2', views.add_book_2),
]

