from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.conf import settings


class Pagination(PageNumberPagination):
    """
    @func：自定义标准分页类
    @param：
        page_size -- 每页数目
        page_query_param -- url中的页码参数，默认为”page”
        page_size_query_param -- url中每页数量参数，默认为"None"
        max_page_size -- 前端最多能设置的每页数量，做限制使用，避免突然大量的查询数据，数据库崩溃
    @return：json
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page_num'
    max_page_size = 100

    def get_my_next(self):
        # print(8888, self.request.path)
        # print(8888, settings.SERVER_NAME)
        # print(8888, self.get_next_link().split(self.request.path))
        return settings.SERVER_NAME + self.request.path + self.get_next_link().split(self.request.path)[1]
    
    def get_my_pre(self):
        return settings.SERVER_NAME + self.request.path + self.get_previous_link().split(self.request.path)[1]

    def get_paginated_response(self, data):
        return Response({
            'errorCode': 0,
            'message': 'ok',
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'data': data
        })
