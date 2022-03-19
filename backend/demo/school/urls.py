from django.urls import path
from demo.school import views
from rest_framework.routers import SimpleRouter

# 1.实例化路由集
router = SimpleRouter()
# 2.注册路由
router.register(prefix='students', viewset=views.StudentModelViewSet, basename='students')
print(f'school/students/router.urls={router.urls}')
# 3.绑定urlpatterns
urlpatterns = router.urls
