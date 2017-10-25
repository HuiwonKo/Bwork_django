from rest_framework import serializers

from meetings.models import Meeting,Participant


class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = ['pk', 'plan', 'time', 'location', ]

class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = ['pk', 'meeting', 'meeting_plan', 'user', 'user_name', 'is_participate', 'participate_time', 'minutes', 'custom_pk', ]

class Meeting_ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = ['user_name', 'is_participate', ]