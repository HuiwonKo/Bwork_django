# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from accounts.models import Profile
from rest_framework.authtoken.admin import TokenAdmin



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'password', )



admin.site.register(Profile, ProfileAdmin)
TokenAdmin.raw_id_fields = ('user', )