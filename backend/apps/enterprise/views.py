# 前提：
# 1）序列化类中不能修改原字段的深度
# 2）通过 data=请求数据包 得到可以操作orm的序列化对象，instance来明确修改的对象，校验成功后还是走save()来更新
# 3）必须先校验，才能保存或更新
from requests import Response

from apps.enterprise.serializer import EnterpriseSerializer
from rest_framework.views import APIView
import json


# GET     /books/         提供所有记录
# POST    /books/         新增一条记录
# GET     /books/<pk>/    提供指定id的记录
# PUT     /books/<pk>/    修改指定id的记录
# DELETE  /books/<pk>/    删除指定id的记录


# 增
class Enterprise(APIView):
    """
    {
        "name":"水浒传",
        "price":"88.88",
        "author":[1, 2, 3 ]
    }
    """

    def get(self, request):
        print('==aaaaaaa==')
        queryset = Enterprise.objects.all()
        serializer = EnterpriseSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        book_dic = json.loads(request.body)
        book_dic = book_dic['data']
        book_json = EnterpriseSerializer(data=book_dic)
        # 数据的校验
        if book_json.is_valid():
            book_json.save()  # 不涉及跨表操作
        return Response({
            'status': 0,
            'msg': 'ok',
            'results': book_json.data
        })
