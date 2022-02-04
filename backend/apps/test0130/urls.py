from django.urls import path
from apps.test0130 import views

# new_list = NewsViewSet.as_view({
#     'get': 'list'
# })
# new_detail = NewsViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]


from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.test0130 import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

