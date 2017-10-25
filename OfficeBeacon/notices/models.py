# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=50, verbose_name='제목')
    content = models.TextField(max_length=300, verbose_name='회사 전체 공지사항')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Notice, self).save(*args, **kwargs)