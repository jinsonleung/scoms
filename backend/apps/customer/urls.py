from django.urls import path
from apps.customer import views


urlpatterns = [
    path('getall', views.get_all),
    path('getpagelist', views.get_page_list),
    # path('add', views.add),
    # path('addbook', views.add_book),
    # path('addbook2', views.add_book_2),
]

