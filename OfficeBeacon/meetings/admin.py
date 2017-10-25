from django.contrib import admin

from meetings.models import Meeting, Participant
# Register your models here.


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'plan', 'time', 'location', 'created_at', 'updated_at', )

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('pk', 'meeting', 'meeting_plan', 'user', 'user_name', 'is_participate', 'participate_time', 'minutes', 'created_at', 'updated_at', )

admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Participant, ParticipantAdmin)