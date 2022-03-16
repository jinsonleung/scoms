from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.student import views


urlpatterns = [
    path('student/', views.StudentAPIView.as_view()),
    path('student/<int:pk>/', views.StudentInfoAPIView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
