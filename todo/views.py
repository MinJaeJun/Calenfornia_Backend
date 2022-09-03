from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSimpleSerializer, TodoDetailSerializer, TodoCreateSerializer #, TodoSerializer

from rest_framework.decorators import api_view
 
class TodosAPIView(APIView):
    # 전체 초회 view // complete가 False Todo들을 필터링, 시리얼라이저를 통하여 형태를 변환하고 Response 형태로 전달 //
    def get(self, request):
        data = request.data
        todos = Todo.objects #(complete=False)인 것 만 필터링
        serializer = TodoSimpleSerializer(todos, many=True) #형태 변환
        return Response(serializer.data, status=status.HTTP_200_OK) #Response 객체 형태로 전달

    # post로 전달받은 데이터를 시리얼라이저를 거쳐서 객체를 만들고 유효성 검사하고 저장하여 유효하지 않을 경우 에러를 출력
    # Todo 생성 뷰
    def post(self, request):
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid(): # 유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 저장합니다.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 에러를 러턴합니다.

class TodoPersonAPIView(APIView):
    def get(self,request, fk):
        data = request.data
        todos = Todo.objects.filter(user_id=fk) # data['user_id']=user_id 인 것을 필터링하여 todos에 저장
        serializer = TodoSimpleSerializer(todos, many=True) # 형태 변환
        return Response(serializer.data, status=status.HTTP_200_OK) #Response 객체 형태로 전달

class TodoAPIView(APIView):
    # 상세 조회 get해서 Todo 객체를 가져오고, 시리얼라이저를 한 뒤 Response를 합니다.
    def get(self, request, pk, fk):
        todos = Todo.objects.filter(user_id=fk)
        todo = get_object_or_404(todos, id = pk) # Todo 객체를 가져온다.
        serializer = TodoDetailSerializer(todo) 
        return Response(serializer.data, status=status.HTTP_200_OK) # Response
    
    # patch() 수정
    def patch(self, request, pk, fk):
        todos = Todo.objects.filter(user_id=fk)
        todo = get_object_or_404(todos, id = pk)
        serializer = TodoDetailSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, fk):
            todos = Todo.objects.filter(user_id=fk)
            todo = get_object_or_404(todos, id = pk)
            # serializer = TodoCreateSerializer(todo)
            todo.delete()
            return Response({"content" : "삭제되었습니다."})

class DonePersonAPIView(APIView):
    def post(self,request):
        data = request.data
        todos = Todo.objects.filter(user_id=data['user_id'], complete=True) # data['user_id']=user_id 인 것을 필터링하여 todos에 저장
        serializer = TodoSimpleSerializer(todos, many=True) # 형태 변환
        return Response(serializer.data, status=status.HTTP_200_OK) #Response 객체 형태로 전달
    
    def get(self, request):
        dones = Todo.objects.filter(complete=True)
        serializer = TodoSimpleSerializer(dones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DonePersonAPIView(APIView):
    def post(self,request):
        data = request.data
        todos = Todo.objects.filter(user_id=data['user_id']) # data['user_id']=user_id 인 것을 필터링하여 todos에 저장
        serializer = TodoSimpleSerializer(todos, many=True) # 형태 변환
        return Response(serializer.data, status=status.HTTP_200_OK) #Response 객체 형태로 전달
    
    def get(self, request):
        dones = Todo.objects.filter(complete=True)
        serializer = TodoSimpleSerializer(dones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['PATCH'])
# @permission_classes([permissions.IsAuthenticated])
# def edit_time(request):

#     if request.method == 'PATCH':
#         serializer = TimeSerializer(request.user, data=request.DATA, partial=True)
#         if serializer.is_valid():
#             time_entry = serializer.save()
#         return Response(status=status.HTTP_201_CREATED) 
#     return Response(status=status.HTTP_400_BAD_REQUEST) 
        # 삭제 기능
    

# 수정 기능 특정 Todo를 찾아서 시리얼라이저에 통과시켜 저장. 유효하지 않으면 에러를 출력     
    #def put(self, request, pk):
        #todo = get_object_or_404(Todo, id=pk)
        #serializer = TodoCreateSerializer(todo, data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_200_OK)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #  
# 체크완료 뷰
class DoneTodosAPIView(APIView):
    # complete가 True인 필터링하여서, 시리얼라이저를 거쳐 Response를 합니다.
    def get(self, request):
        dones = Todo.objects.filter(complete=True)
        serializer = TodoSimpleSerializer(dones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def delete(self, request):
    # todo = get_object_or_404(Todo, id)
    # todo.delete()
    # return Response(status=status.HTTP_204_NO_CONTENT)

# 체크완료 저장 뷰
class DoneTodoAPIView(APIView):
    def get(self, request, pk):
        done = get_object_or_404(Todo, id=pk)
        done.complete = True
        done.save()
        serializer = TodoDetailSerializer(done)
        return Response(status=status.HTTP_200_OK)




#@api_view(["GET"])
#def todolist(req):
#    todos = Todo.objects.all()
#    serializer = TodoSerializer(todos, many=True)
#    return Response(serializer.data)


#@api_view(["POST"])
#def todocreate(req):
#    serializer = TodoSerializer(data=req.data)
#    if serializer.is_valid():
#        serializer.save()
#        return Response(serializer.data)
#    return Response(serializer.errors)


#@api_view(["DELETE"])
#def tododelete(req, pk):
#    todo = Todo.objects.get(id=pk)
#    todo.delete()
#    return Response("Delete Success")


#@api_view(["PATCH"])
#def todoupdate(req, pk):
#    todo = Todo.objects.get(id=pk)
#    serializer = TodoSerializer(todo, data=req.data)
#    if serializer.is_valid():
#        serializer.save()
#        return Response(serializer.data)
#    return Response(serializer.errors)