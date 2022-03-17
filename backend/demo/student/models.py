from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False, verbose_name='姓名', db_index=True)
    age = models.IntegerField(blank=True, null=True, verbose_name='年龄')

    class Meta:
        db_table = 'student'
        verbose_name = '学生表'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name





