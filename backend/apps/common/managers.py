from django.db import models
from django.db.models import QuerySet


class SoftDeleteQuerySet(QuerySet):
    """软删除QuerySet"""
    def delete(self):   # 重写delete()，软删除
        return super(SoftDeleteQuerySet, self).update(is_delete=True)

    def hard_delete(self):  # 硬删除
        return super(SoftDeleteQuerySet, self).delete()


class CommonManager(models.Manager):
    """支持软删除"""
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model).filter(is_delete=False)
