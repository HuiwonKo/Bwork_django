# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from __future__ import unicode_literals

from django.core.mail import send_mail
from django.db import models


class Profile(AbstractUser):

    id = models.AutoField(primary_key=True)
    # Extra user information fields
    nick = models.CharField(max_length=20, verbose_name='닉네임')
    phone = models.CharField(max_length=20, verbose_name='전화번호')
    is_flextime = models.BooleanField(default=False, verbose_name='자율출퇴근제 사용 여부')
    flextime = models.CharField(max_length=20, default=0, verbose_name='자율출퇴근제 시간')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일자')
    # 알림시간 - 사용자 정의 가능하게 할건지 // 마감 1시간 전, 마감 3시간 전 )

    # Token 발급
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    def __unicode__(self):
        return '%s' % (self.username)


    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def clean(self):
        super(AbstractUser, self).clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


"""

#case 2 : one to one mapping with Django User Model
class Profile(models.Model):

    # Mapping with Django AUTH USER MODEL
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')

    # Extra user information fields
    nick = models.CharField(max_length=20, verbose_name='닉네임')
    phone = models.CharField(max_length=20, verbose_name='전화번호')
    is_flextime = models.BooleanField(default=False, verbose_name='자율출퇴근제 사용 여부')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일자')

    # 알림시간 - 사용자 정의 가능하게 할건지 // 마감 1시간 전, 마감 3시간 전 )
"""
