from .models import UserSubject
from .serializers import UserSubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from subjects.models import Subject
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

# Create your views here.
class UsersSubjectView(APIView):
    def get(self,request):
        data = request.data
        subjects = UserSubject.objects.all()
        serializer = UserSubjectSerializer(subjects,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = UserSubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserSubjectView(APIView):
    #상세 조회
    def get(self, request, fk):
        subjects = UserSubject.objects.filter(user_id=fk)
        serializer = UserSubjectSerializer(subjects,many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, fk):
        subjects = UserSubject.objects.filter(user_id=fk)
        subjects.delete()
        return Response({"message":"삭제되었습니다."})


class UserEditView(APIView):
    def get(self, request, fk, pk):
        subjects = UserSubject.objects.filter(user_id=fk)
        subject = get_object_or_404(subjects, id = pk)
        serializer = UserSubjectSerializer(subject)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, fk, pk):
        subjects = UserSubject.objects.filter(user_id=fk)
        subject = get_object_or_404(subjects, id = pk)
        serializer = UserSubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # 삭제
    def delete(self, request, fk, pk):
        subjects = UserSubject.objects.filter(user_id=fk)
        subject = get_object_or_404(subjects, id=pk)
        subject.delete()
        return Response({"message":"삭제되었습니다."})
