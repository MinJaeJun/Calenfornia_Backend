from django.forms import ValidationError
from django.http import Http404
from rest_framework import serializers
from django.contrib.auth import get_user_model
import bcrypt
import requests
from .models import Classnet, User

# 홍익대학교 인증 
def signin_with_hongik(user_id, user_pw):
    res = requests.post(
        'https://ap.hongik.ac.kr/login/LoginExec3.php',
        data={'USER_ID': user_id, 'PASSWD': user_pw}
    )
    res.raise_for_status()
    return False if res.text.find('SetCookie') == -1 else True

# 로그인
class SignupSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        new_salt = bcrypt.gensalt()    
        new_password = validated_data["classnetpw"].encode('utf-8')

        hashed_password = bcrypt.hashpw(new_password, new_salt)

        user = User.objects.create(
            classnetid=validated_data["classnetid"],
            classnet=validated_data["classnet"],
            classnetpw=hashed_password.decode()
        )   

        user.save()

        return user

    class Meta:
        model = User
        fields = ['pk', 'classnet', 'classnetid', 'classnetpw']

# Classnet
class ClassnetSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        qs = Classnet.objects.all()
        qs.delete()
        classnet_id = validated_data["classnetid"]
        classnet_pw = validated_data["classnetpw"]

        classnet_ok = signin_with_hongik(classnet_id, classnet_pw)
        
        if classnet_ok == True:
            Classnet.objects.create(
             classnet = classnet_ok,  
             classnetid = classnet_id,
            )
            return True

        else:
            raise Http404

    class Meta:
        model = Classnet
        fields = ['classnet', 'classnetid', 'classnetpw']