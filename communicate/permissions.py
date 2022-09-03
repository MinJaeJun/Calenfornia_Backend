from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

from .models import Comment
from .serializers import CommentSerializer, CommentCreateSerializer, CommentDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Info
from rest_framework import status

from rest_framework.generics import get_object_or_404

class CommentsAPIView(APIView):
    #전체 조회
    def get(self,request):
        comments = Info.objects.all()
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    #post
    def post(self, request):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CommentAPIView(APIView):
    #상세 조회
    def get(self, request, pk,fk):
        comments = Info.objects.filter(user_id=fk)
        comment = get_object_or_404(comments, info_id = pk)
        serializer = CommentDetailSerializer(comment) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 수정
    def patch(self, request, pk,fk):
        comments = Info.objects.filter(user_id=fk)
        comment = get_object_or_404(comments, info_id = pk)
        serializer = CommentCreateSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # 삭제
    def delete(self, request, pk,fk):
        comments = Info.objects.filter(user_id = fk)
        comment = get_object_or_404(comments, info_id=pk)
        comment.delete()
        return Response({"message":"삭제되었습니다."})

# user 필터링
class UserCommentView(APIView):
    def get(self,request,fk):
        data = request.data
        comment = Info.objects.filter(user_id=fk)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

# # (댓글) Comment 보여주기, 수정하기, 삭제하기 모두 가능
# class CommentViewSet(viewsets.ModelViewSet):
#     authentication_classes = [BasicAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

#     def get_serializer_class(self):
#         if self.action == 'list' or 'retrieve':
#             return CommentSerializer
#         return CommentCreateSerializer
    
#     def perform_create(self, serializer):
#         serializer.save(user = self.request.user)

# # (게시글) Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
# # class CommnetInfoViewSet(viewsets.ModelViewSet):
# #     authentication_classes = [BasicAuthentication, SessionAuthentication]
# #     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
# #     queryset = CommnetInfo.objects.all()
# #     serializer_class = CommnetInfoSerializer
    
# #     def get_serializer_class(self):
# #         if self.action == 'list' or 'retrieve':
# #             return CommnetInfoSerializer
# #         return CommnetInfocreateSerializer
    
# #     def perform_create(self, serializer):
# #         serializer.save(user = self.request.user)