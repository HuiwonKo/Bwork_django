# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from notices.models import Notice

# Register your models here.


class NoticeAdmin(admin.ModelAdmin):
    fields = ('title', 'content', )
    list_display = ('title', 'content', )

admin.site.register(Notice,NoticeAdmin)

