from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from demo.student import views


""" 
1. 普通路由
"""
# urlpatterns = [
#     # 1.基本视图APIView的路由
#     path('student/', views.StudentAPIView.as_view()),
#     path('student/<int:pk>/', views.StudentInfoAPIView.as_view()),
#     # 2通用视图GenericAPIView的路由
#     path('student2/', views.StudentGenericAPIView.as_view()),
#     path('student2/<int:pk>/', views.StudentInfoGenericAPIView.as_view()),
#     # 3.扩展视图（混入视图）Mixins的路由
#     path('student3/', views.StudentMixinAPIView.as_view()),
#     path('student3/<int:pk>/', views.StudentInfoMixinAPIView.as_view()),
#     # 4.视图子类的路由，GenericAPIView+Mixins的子类
#     path('student4/', views.StudentView.as_view()),
#     path('student4/<int:pk>/', views.StudentInfoView.as_view()),
#     # 5.普通视图集 ViewSet
#     # 说明：as_view()函数已被改造，需要actions作为参数（字典格式参数），调用如下
#     # path('student5/', views.StudentViewSet.as_view({"http请求动作", "视图方法"})),
#     path('student5/', views.StudentViewSet.as_view(
#         {"get": "get_student_list",
#          "post": "create",  # 可自定义方法名，也可以原来方法名
#          })),
#     path('student5/<int:pk>/', views.StudentViewSet.as_view(
#         {"get": "get_student",
#          "put": "update",  # 可自定义方法名，也可以原来方法名
#          "delete": "delete",    # 也可同名
#          })),
#     # 6.通用视图集 GenericViewSet
#     # 说明：as_view()函数已被改造，需要actions作为参数（字典格式参数），调用如下
#     # path('student5/', views.StudentViewSet.as_view({"http请求动作", "视图方法"})),
#     path('student6/', views.StudentGenericViewSet.as_view(
#         {"get": "list",
#          "post": "create",  # 可自定义方法名，也可以原来方法名
#          })),
#     path('student6/<int:pk>/', views.StudentGenericViewSet.as_view(
#         {"get": "get_student",
#          "put": "update",  # 可自定义方法名，也可以原来方法名
#          "delete": "destroy",  # 可自定义方法名
#          })),
#     # 7.通用视图集 GenericViewSet+Mixin
#     # 说明：as_view()函数已被改造，需要actions作为参数（字典格式参数），调用如下
#     # path('student5/', views.StudentViewSet.as_view({"http请求动作", "视图方法"})),
#     path('student7/', views.StudentMixinGenericViewSet.as_view(
#         {"get": "list",
#          "post": "create",  # 可自定义方法名，也可以原来方法名
#          })),
#     path('student7/<int:pk>/', views.StudentMixinGenericViewSet.as_view(
#         {"get": "retrieve",
#          "put": "update",  # 可自定义方法名，也可以原来方法名
#          "delete": "destroy",  # 可自定义方法名
#          })),
#     # 8.ReadOnly视图集，ReadOnlyModelViewSet(实现了2个查询接口，查询所有记录及查询一条记录)
#     path('student8/', views.StudentReadOnlyModelViewSet.as_view(
#         {"get": "list",
#          "post": "create",
#          })),
#     path('student8/<int:pk>/', views.StudentReadOnlyModelViewSet.as_view(
#         {"get": "retrieve",
#          "put": "update",
#          "delete": "destroy",
#          })),
#     # 9.Model视图集，ModelViewSet(最终版，实现了全部5个接口)
#     path('student9/', views.StudentModelViewSet.as_view(
#         {"get": "list",
#          "post": "create",
#          })),
#     path('student9/<int:pk>/', views.StudentModelViewSet.as_view(
#         {"get": "retrieve",
#          "put": "update",
#          "delete": "destroy",
#          })),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)


"""
2. 路由集 Routers
- 自动生成路由信息，与视图集一起使用，不能跟非视图集一起使用
- SimpleRouter与DefaultRouter没什么区别
"""

# from rest_framework.routers import SimpleRouter
# # 2.1 实例化路由类
# router = SimpleRouter()
# # 2.2 注册路由，参数prefix必须是字符串不能是正则表达式，basename一般与prefix一样即可
# router.register('student10', views.StudentModelViewSet, basename='student10')
# # router.register('student11', views.StudentModelViewSet, basename='student11')
# print(router.urls)
# # 2.3 把生成的路由绑定给urlpatterns
# urlpatterns = router.urls




"""
3. 路由集 Routers + 自动API接口文档生成
- 自动生成路由信息，与视图集一起使用，不能跟非视图集一起使用
- SimpleRouter与DefaultRouter没什么区别
"""


from rest_framework.routers import SimpleRouter
# 3.1 实例化路由类
router = SimpleRouter()
# 3.2 注册路由，参数prefix必须是字符串不能是正则表达式，basename一般与prefix一样即可
router.register('student10', views.StudentModelViewSet, basename='student10'),

print(router.urls)
# 3.3 把生成的路由绑定给urlpatterns
urlpatterns = router.urls


