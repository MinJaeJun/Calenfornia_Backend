from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import resolve_url


class Classnet(models.Model):
    # classnet Class
    classnet = models.BooleanField(default=False)
    classnetid = models.CharField(default='', max_length=100, null=False, blank=False)
    classnetpw = models.CharField(default='', max_length=100, null=False, blank=False)


class User(models.Model):
    # 기본 : 아이디(username) 암호(password) 
    classnet = models.BooleanField(default=False)
    classnetid = models.CharField(unique=True, default='',max_length=100, null=False, blank=False)
    classnetpw = models.CharField(default='', max_length=100, null=False, blank=False)
    
    
    # avatar = models.ImageField(blank=True, upload_to="accounts/avatar/%y/%m", 
    # help_text="48px * 48px 크기의 png/jpg 파일을 업로드해주세요")
    # @property
    # def avatar_url(self):
    #     if self.avatar:
    #         return self.avatar.url
    #     else:
    #         return resolve_url("pydenticon_image", self.username)
    # 