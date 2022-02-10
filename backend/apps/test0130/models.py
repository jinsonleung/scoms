from django.db import models


# 新闻类，用于测试
class News(models.Model):
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'news'  # 修改表名
        verbose_name = '新闻表'  # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['name']  # 排序字段

    def __str__(self):
        return self.name


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
