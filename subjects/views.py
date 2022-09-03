from django.shortcuts import render
from .models import Subject
from .serializers import SubjectSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

class SubjectsAPIView(APIView):
    #전체 조회
    def get(self,request):
        subject = Subject.objects.all()
        serializer = SubjectSerializer(subject,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    #post
    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class SubjectAPIView(APIView):
    #상세 조회
    def get(self, request, pk):
        subject = get_object_or_404(Subject, id = pk)
        serializer =SubjectSerializer(subject) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
