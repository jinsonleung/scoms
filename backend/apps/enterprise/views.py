from django.http import QueryDict
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from utils.pagination import Pagination
from apps.enterprise.models import Enterprise
from apps.enterprise.serializers import EnterpriseSerializer
from rest_framework import mixins, status
from rest_framework import generics
import json


class EnterpriseList0(generics.ListAPIView):
    print('ddddd')
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    pagination_class = Pagination


class EnterpriseList(generics.ListAPIView,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    """
    列出所有的记录，或创建一条新的记录。
    """
    # queryset = Enterprise.objects.all()   # 获取所有记录
    queryset = Enterprise.custom.all()  # 获取非软删、除的记录
    serializer_class = EnterpriseSerializer  # 序列化
    pagination_class = Pagination  # 分页

    def get(self, request, *args, **kwargs):
        """获取分页数据"""
        print('==get all==', request.data)
        return self.list(request, *args, **kwargs)

    # @staticmethod
    # def get(self, request, *args, **kwargs):
    #     print('==request.data==', request.data)
    #     queryset = Enterprise.objects.all()
    #     serializer_class = EnterpriseSerializer
    #     pagination_class = Pagination
    #
    #     # all_objects = self.queryset
    #     # page_objects = Pagination.paginate_queryset(self=self, queryset=all_objects, request=request, view=self)
    #     # page_serializer = EnterpriseSerializer(instance=page_objects, many=True)
    #
    #
    #     # return Response(page_serializer.data)
    #     # all_objects = Enterprise.custom.all()
    #     # page_objects = Pagination.paginate_queryset(queryset=all_objects, request=request, self=all_objects)
    #     # page_serializer = EnterpriseSerializer(instance=page_objects, many=True)
    #     # return Response(page_serializer.data)
    #     return Response({'result_message': 'failure', 'result_code': 404, 'result_body': 'delete failed'})
    #     # return self.create(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('==post==', type(request.data),request.data)
        return self.create(request, *args, **kwargs)


class EnterpriseDetail(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    """
    获取、更新或删除一条记录
    """
    # queryset = Enterprise.objects.all()   # 获取所有记录
    queryset = Enterprise.custom.all()  # 获取非软删除的记录
    serializer_class = EnterpriseSerializer

    def get(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def put_0(self, request, *args, **kwargs):
        print('==put，request.data==', type(request.data), request.data)
        return self.update(request, *args, **kwargs)

    def put_1(self, request, *args, **kwargs):
        # print('==put，request.get_full_path()==', request.get_full_path())
        print('==put，request.data==', type(request.data), request.data)
        # data1 = dict_to_querydict(request.data)
        # print('==put，data1==', type(data1), data1)
        # request.QueryDict.dict = data1
        # print('==put，request.data2==', type(request.data), request.data)
        # print('==put，request.data[id]==', request.data['id'])

        # 以下更新成功，返回个别字段是必须的问题，如create_by字段
        # enterprise = Enterprise.custom.get(id=request.data['id'])
        # print('==id==', request.data['id'])

        # serializer = EnterpriseSerializer(enterprise, data=request.data)
        # # print('==put，serializer==', serializer.is_valid, serializer)
        # # if serializer.is_valid():
        # #     serializer.save()
        # #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'result_message': 'failure', 'result_code': 404, 'result_body': 'delete failed'})

    def put(self, request, *args, **kwargs):
        print('=====put=======')
        # # res1 = json.loads(request.body)
        # # print('==put，res1==', res1)
        # # res1_data = res1['data']  # dict
        # # print('==put，res1_data==', res1_data)
        # # res1_sl = EnterpriseSerializer(data=res1_data)
        # # if res1_sl.is_valid():
        # #     return Response({'message': True})
        # # return Response({'result_message': 'failure', 'result_code': 404, 'result_body': 'delete failed'})
        # instance = Enterprise.objects.filter(id=kwargs.get('pk')).first()
        # print('==instance==', instance)
        #
        # data = request.data
        # city1 = data.get('city')
        # print('==city1==', type(city1), city1)
        # # request.data['city'] = '[\'' + request.data['city'] + ']\''
        # # request.data['city'] = '[\'[\'' + '\',\''.join(request.data['city']) +']\']\''
        # # request.data['city'] = '[\'' + '\',\''.join(request.data['city']) + '\']'
        # # if request.data['city']: request.data['city'] = ','.join(request.data['city'])
        #
        # city2 = data.get('city')
        # print('==city2==', type(city2), city2)

        return self.update(request, *args, **kwargs)

    @staticmethod
    def delete_0(request, *args, **kwargs):
        """
        @func：重写delete，软删除一条记录，DELETE请求，如DELETE enterprise/111，正确
        @param：id
        @return：json
        """
        pk = kwargs.get('pk')
        delete_obj = Enterprise.custom.filter(pk=pk).update(is_delete=True)
        if delete_obj:
            return Response({'result_message': 'success', 'result_code': 200, 'result_body': 'deleted successfully'})
        return Response({'result_message': 'failure', 'result_code': 404, 'result_body': 'delete failed'})

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


def dict_to_querydict(dict_data):
    qdict = QueryDict('', mutable=True)
    for key, value in dict_data.items():
        if isinstance(value, list):
            qdict.setlist(key, value)
        else:
            qdict[key] = value
    return qdict
