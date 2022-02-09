from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.enterprise import views

# """
# @func：企业记录接口
# """
urlpatterns = [
    path('enterprise', views.EnterpriseList.as_view()),
    path('enterprise/<int:pk>', views.EnterpriseDetail.as_view()),
    ]
urlpatterns = format_suffix_patterns(urlpatterns)



