from rest_framework import serializers
from .models import Info

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields =['id','user_id','subject_id','professor_id','classnum','category_id','date','title','description','edit_time']

class InfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['id','user_id','subject_id','professor_id','classnum','category_id','date','title','description','edit_time']

class InfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['id','user_id','subject_id','professor_id','classnum','category_id','date','title','description','edit_time']


class InfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['id','user_id','subject_id','professor_id','classnum','category_id','date','title','description','edit_time']


class SubjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['info_id','user_id','subject_id','professor_id','classnum','category_id','date','title','description','edit_time']