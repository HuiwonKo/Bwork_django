# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from commutes.models import Commute
# Register your models here.



class CommuteAdmin(admin.ModelAdmin):
    list_display = ('user', 'pk', 'is_in', 'is_out', 'in_time', 'out_time', 'shift', )

    def __init__(self, model, admin_site):
        self.model = model
        self.opts = model._meta
        self.admin_site = admin_site
        super(ModelAdmin, self).__init__()

    def __str__(self):
        return "%s.%s" % (self.model._meta.app_label, self.__class__.__name__)


admin.site.register(Commute, CommuteAdmin)