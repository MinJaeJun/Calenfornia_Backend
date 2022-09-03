from rest_framework import serializers
from .models import UserSubject

class UserSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubject
        fields = ("id","user_id","subject_id","professor_id","classnum")