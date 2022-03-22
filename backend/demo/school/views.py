from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from demo.school.models import Student
from demo.school.serializers import StudentModelSerializer


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    # def get(self, request):
    #     return Response({'msg': '获取成功'})
