from django.db import models
from accounts.models import User
from subjects.models import Subject

class Info(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject,on_delete = models.CASCADE)
    professor_id = models.IntegerField()
    classnum = models.IntegerField() # 분반
    category_id = models.IntegerField()
    date = models.DateField()
    title = models.CharField(max_length=50) 
    description = models.TextField()
    edit_time = models.DateTimeField(auto_now=True)