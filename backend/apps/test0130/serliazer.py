from rest_framework import serializers
from apps.test0130.models import News
from apps.test0130.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# 序列货器
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News   # 序列化的对象名
        fields = '__all__'  # 序列货所有字段


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

