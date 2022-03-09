from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.universalCode import views

# """
# @func：接口URL
# """


urlpatterns = [
    path('airport/', views.AirportList.as_view()),
    path('airport/<int:pk>', views.AirportDetail.as_view()),
    path('airline/', views.AirlineList.as_view()),
    path('country/', views.CountryList.as_view()),
    # path('airport/<int:pk>', views.AirportDetail.as_view()),

    ]
urlpatterns = format_suffix_patterns(urlpatterns)



