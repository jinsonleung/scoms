from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.freightTools.airport11 import views

# """
# @func：接口URL
# """
urlpatterns = [
    path('airport11/', views.AirportList.as_view()),
    path('airport11/<int:pk>', views.AirportDetail.as_view()),
    ]
urlpatterns = format_suffix_patterns(urlpatterns)



