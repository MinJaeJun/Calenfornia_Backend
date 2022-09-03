from django.db import models
from accounts.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Todo(models.Model):
    description = models.TextField(blank=True)                  # 설명
    created = models.DateTimeField(auto_now_add=True)           # 생성일자
    complete = models.BooleanField(default=False)               # 완료 여부
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.description # 설명 반환

# class Todos(models.Model):
#    id = models.AutoField(primary_key=True)
#    description = models.CharField(max_length=50)