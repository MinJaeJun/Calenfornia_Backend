from .models import Info
from .serializers import InfoSerializer, InfoCreateSerializer, InfoDetailSerializer,SubjectInfoSerializer
from usersubject.models import UserSubject
from usersubject.serializers import UserSubjectSerializer
from rest_framework import status
from .serializers import InfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
import sys
sys.path.append("..")

class InfosAPIView(APIView):
    #전체 조회
    def get(self,request):
        infos = Info.objects.all()
        serializer = InfoSerializer(infos,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    #post
    def post(self, request):
        serializer = InfoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class InfoAPIView(APIView):
    #상세 조회
    def get(self, request, pk):
        info = get_object_or_404(Info, id = pk)
        serializer = InfoDetailSerializer(info) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 수정
    def patch(self, request, pk):
        info = get_object_or_404(Info, id = pk)
        serializer = InfoCreateSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # 삭제
    def delete(self, request, pk):
        info = get_object_or_404(Info, id=pk)
        info.delete()
        return Response({"message":"삭제되었습니다."})


class UserSubjectInfoView(APIView):
    def get(self,request,fk):
        subjects = UserSubject.objects.filter(user_id=fk)
        userserializer = UserSubjectSerializer(subjects,many=True) 

        # user가 저장한 필터 적용 과목 리스트 가져오기
        userSubject = list(map(lambda n : n['subject_id'], userserializer.data))
        subjectProf = list(map(lambda n : n['professor_id'], userserializer.data))
        profClassNum = list(map(lambda n : n['classnum'], userserializer.data))

        info = Info.objects
        result = []

        # 과목 리스트의 인덱스에 해당하는 과목, 교수, 분반과 일치하는 Info의 데이터가 있는지 조회 후 filter
        # 이후에 result 배열에 serializer로 변환하고 데이터 저장
        for i in range(len(userSubject)):
            tmp = Info.objects.filter(subject_id=userSubject[i], professor_id=subjectProf[i], classnum=profClassNum[i])
            tmpserializer = InfoSerializer(tmp,many=True) 
            if len(tmpserializer.data) != 0:
                result.append(tmpserializer.data)

        info = info.filter(subject_id=userSubject[0])
        
        return Response(result, status=status.HTTP_200_OK)


class UserInfoView(APIView):
    def get(self,request,fk):
        data = request.data
        info = Info.objects.filter(user_id=fk)
        serializer = InfoSerializer(info,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class SubjectInfoView(APIView):
    def get(self,request,fk):
        data = request.data
        infos = Info.objects.filter(subject_id = fk)
        serializer = SubjectInfoSerializer(infos, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)