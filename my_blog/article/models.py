# -*- coding:utf-8 -*-


from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    # 获取URL并转换成URL的表示格式
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.01:8000%s" % path

    # 使用title来表示Article对象
    def __str__(self):
        return self.title

    # 按时间下降排序
    class Meta:
        ordering = ['-date_time']