from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.test0130.serliazer import NewsSerializer
from apps.test0130.models import News
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.test0130.models import Snippet
from apps.test0130.serliazer import SnippetSerializer
from rest_framework.parsers import JSONParser


# class NewsViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list` and `retrieve` actions.
#     """
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer


from rest_framework import generics


from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

