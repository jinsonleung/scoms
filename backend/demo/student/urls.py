from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from demo.student import views

urlpatterns = [
    # 1.基本视图APIView的路由
    path('student/', views.StudentAPIView.as_view()),
    path('student/<int:pk>/', views.StudentInfoAPIView.as_view()),
    # 2通用视图GenericAPIView的路由
    path('student2/', views.StudentGenericAPIView.as_view()),
    path('student2/<int:pk>/', views.StudentInfoGenericAPIView.as_view()),
    # 3.扩展视图（混入视图）Mixins的路由
    path('student3/', views.StudentMixinAPIView.as_view()),
    path('student3/<int:pk>/', views.StudentInfoMixinAPIView.as_view()),
    # 4.视图子类的路由，GenericAPIView+Mixins的子类
    path('student4/', views.StudentView.as_view()),
    path('student4/<int:pk>/', views.StudentInfoView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
