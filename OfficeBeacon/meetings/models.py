from django.db import models
from accounts.models import Profile
from datetime import datetime
from django.contrib.auth.models import User
from accounts.models import Profile




DEFAULT_USER_PK = 1
#DEFAULT_USER = Profile.objects.get(username='admin')




class Meeting(models.Model):

    id = models.AutoField(primary_key=True)
    plan = models.CharField(max_length=150, verbose_name='회의 이름')
    time = models.CharField(max_length=100, verbose_name='회의 날짜')
    location = models.CharField(max_length=150, verbose_name='회의 장소')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일자')

    def __unicode__(self):
        return '%s' % (self.plan)

    # overriding save method
    def save(self, *args, **kwargs):
        print("meeting_pk")
        print(self.pk)
        super(Meeting, self).save(*args, **kwargs)


class Participant(models.Model):

    def __unicode__(self):
        return '%s' % (self.user.username)

    def get_meeting_plan(self):
        return self.meeting.plan

    # @staticmethod
    def get_custom_pk(self):
        return str(self.meeting.pk) + '-' + str(self.user.pk)

    def get_user(self):
        user_object = Profile.objects.get(username=self.user_name)
        return user_object.pk

    def get_user_name(self):
        return self.user.username


    meeting = models.ForeignKey(Meeting, related_name='participant_meeting',
                        verbose_name='meeting PK')  # 1(meeting)대 N(participant) 연결
    meeting_plan = get_meeting_plan

    user = models.ForeignKey(Profile, related_name='participant_user', null=True, verbose_name='user PK')  # 1대1 연결
    #user_name = models.CharField(max_length=30, default='', verbose_name='참석자 이름')
    user_name = get_user_name

    is_participate = models.BooleanField(default=False, verbose_name='참석 여부')
    participate_time = models.DateTimeField(default=datetime.now, verbose_name='참석한 시간')
    minutes = models.TextField(default='회의록을 적어주세요', max_length=500, verbose_name='회의')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일자')

    custom_pk = models.CharField(max_length=30, default='', primary_key=True)








    # overriding save method
    def save(self, *args, **kwargs):
        self.custom_pk = self.get_custom_pk()
        #self.user = self.get_user()
        super(Participant, self).save(*args, **kwargs)



