from django.db import models

class Subject(models.Model):
    subject_title = models.TextField()
    professor = models.TextField()
    classnum = models.TextField()