from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.universalCode import views

# """
# @func：接口URL
# """


urlpatterns = [
    path('universalCode/airport/', views.AirportList.as_view()),
    path('universalCode/airport/<int:pk>', views.AirportDetail.as_view()),
    ]
urlpatterns = format_suffix_patterns(urlpatterns)



