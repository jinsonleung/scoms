from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.conf import settings


class Pagination(PageNumberPagination):
    """
    @func：自定义标准分页类
    @param：
        pageSize -- 每页数目
        page_query_param -- url中的页码参数，默认为”page”
        page_size_query_param -- url中每页数量参数，默认为"None"
        max_page_size -- 前端最多能设置的每页数量，做限制使用，避免突然大量的查询数据，数据库崩溃
    @return：json
    """
    pageSize = 10
    page_size_query_param = 'pageSize'
    page_query_param = 'pageNum'
    max_page_size = 100

    def get_my_next(self):
        return settings.SERVER_NAME + self.request.path + self.get_next_link().split(self.request.path)[1]
    
    def get_my_pre(self):
        return settings.SERVER_NAME + self.request.path + self.get_previous_link().split(self.request.path)[1]

    def get_paginated_response(self, data):
        """自定义分页参数"""
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('page', self.page.number),
            ('totalPage', self.page.paginator.num_pages),
            ('pageSize', self.page.paginator.per_page),
            ('data', data)
        ]))

