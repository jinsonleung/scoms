from rest_framework import serializers
from demo.books.models import Books
from rest_framework.serializers import BaseSerializer


# 图书类序列货器
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books   # 序列化的对象名
        fields = '__all__'  # 序列货所有字段

