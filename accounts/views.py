from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from django.views import View
from .serializers import  SignupSerializer,ClassnetSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,Classnet
from django.http import Http404, JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from . import serializers
import requests
import json
import bcrypt
import jwt
import sys
sys.path.append("..")
from backend.settings import SECRET_KEY

#post response로 True False만을 보내주세요. 
class SignupView(CreateAPIView): # get -> post로 변경해주세여 제발!
    model = User
    serializer_class = SignupSerializer
    permission_classes = [
        AllowAny,
    ]

    def get(self, request):
        signup_auth = User.objects.last()
    
        try:
            serializer = SignupSerializer(signup_auth)
            return Response(serializer.data, status=200)
    
        except ObjectDoesNotExist:
            return Http404

class LoginView(APIView):
    model = User
    queryset = ''
    serializer_class = SignupSerializer

    def post(self, request):
        data = request.data

        try:
            if User.objects.filter(classnetid = data['classnetid']).exists():
                user = User.objects.get(classnetid = data['classnetid'])
                if bcrypt.checkpw(data['classnetpw'].encode('utf-8'), user.classnetpw.encode('utf-8')):
                    token = jwt.encode({'user_id' : user.id}, SECRET_KEY, algorithm = "HS256")
                    token = token.decode('utf-8')                          # 유니코드 문자열로 디코딩
                    #-----------------------------#
                    # return JsonResponse({"token" : token }, status=200)    # 토큰을 담아서 응답
                    payload = jwt.decode(token, SECRET_KEY, "HS256")
                    return Response({"id" : user.id, "token" : token}, status=200)
                else :
                    return HttpResponse(status=401)

            return HttpResponse(status=400)
        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status = 400)

class ClassnetView(ListCreateAPIView): # classnet 인증
    model = Classnet
    queryset = ''
    serializer_class = ClassnetSerializer
    permission_classes = [
        AllowAny,
    ]

    def get(self,request):
        class_auth = Classnet.objects.last()
        
        try:
            serializer = ClassnetSerializer(class_auth)
            return Response(serializer.data, status=200)

        except ObjectDoesNotExist:
            return Http404

def home(request):
    return render(request, 'index.html')


    #def get(self, request):
    #    class_auth = Classnet.objects.last()
    
    #    try:
    #        serializer = ClassnetSerializer(class_auth)
    #        return Response(serializer.data)

    #    except ObjectDoesNotExist:
    #        return Http404

    # def post()
    
# class ClassnetView(APIView):
#     permission_classes = [AllowAny]

#     def post(self,request):
#         req = json.loads(request.body.decode('utf-8'))
#         classnet_id = req['classnet_id']
#         classnet_pw = req['classnet_pw']
#         classnet_ok = signin_with_hongik(classnet_id,classnet_pw)
#         if classnet_ok==True:










