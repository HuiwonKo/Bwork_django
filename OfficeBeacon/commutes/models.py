# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from accounts.models import Profile

# Create your models here.

class Commute(models.Model):

    user = models.ForeignKey(Profile, related_name='commute_user', on_delete=models.CASCADE)
    is_in = models.BooleanField(default=False, verbose_name='출근 여부')
    is_out = models.BooleanField(default=False, verbose_name='퇴근 여부')
    in_time = models.DateTimeField(max_length=30, blank=True, verbose_name='출근 시간')
    out_time = models.DateTimeField(max_length=30, default=datetime.now, blank=True, verbose_name='퇴근 시간')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='생성일자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일자')
    shift = models.CharField(default='', max_length=50, verbose_name='근무 시간')

    def get_shift(self):
        print(self.in_time)
        return (self.out_time - self.in_time)

    def get_user_name(self):
        return self.user.username

    def get_custom_pk(self):
        created_date = datetime.now().strftime('%Y%m%d')  # created_date = 생성날짜 2017-02-16 format => 20170216
        return str(self.user.pk) + '-' + created_date

    custom_pk = models.CharField(max_length=30, default='', primary_key=True)

    def save(self, *args, **kwargs):
        self.custom_pk = self.get_custom_pk()
        print(self.in_time)
        print("commute_pk")
        print(self.pk)
        super(Commute, self).save(*args, **kwargs)

"""
class ConvertingDateTimeField(models.DateTimeField):

    def get_prep_value(self, value):
        return str(datetime.strptime(value, '%Y/%m/%d %H:%M:%S'))
"""

"""

    def save(self, *args, **kwargs):
        self.created_date = self.created_at[:10]
        super(Commute, self).save(*args, **kwargs)


    def __unicode__(self):
        return '%s : %s' % (self.user, self.created_date)
    """