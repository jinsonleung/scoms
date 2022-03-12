from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.supplier import views

# """
# @func：接口URL
# """


urlpatterns = [
    path('supplier/', views.SupplierList.as_view()),
    path('supplier/<int:pk>', views.SupplierDetail.as_view()),
    ]
urlpatterns = format_suffix_patterns(urlpatterns)
