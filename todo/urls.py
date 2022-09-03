from django.urls import path
from .views import * 
from .views import TodoAPIView, TodosAPIView, DoneTodoAPIView, DoneTodosAPIView, TodoPersonAPIView
from accounts.models import User
from .models import Todo
# 어 내가 알기로는 잘 모르지만 프론트에서 post나 get을, 사용자를 식별할 수 있는 token, header에 넣어서 보여주는...
# todo/user_id/todo_id
# post를 해서 user에 대한 것을 해줄테니까 .filtering 해서,  
urlpatterns = [
    path('todo/', TodosAPIView.as_view()),  
    path('todo/<int:fk>/', TodoPersonAPIView.as_view()),  
    path('todo/<int:fk>/<int:pk>/', TodoAPIView.as_view()),

    # path('todo/<int:pk>/<int:pk>', TodoAPIView.as_view(), )
    # todo를...... 어떻게 짜야 할 까....
    # 사용자의 pk 를 연결...... // 설명에 대한 하나하나의 부분을 다 pk 처리? 
    # 사용자에 대한 pk를 하나 // 설명에 대한 부분을 하나하나 다 넣어놔야 할 것 같고
    # 최종목표는 토큰을 반영하는 것이다. 

    path('done/', DoneTodosAPIView.as_view()),
    path('done/<int:pk>/', DoneTodoAPIView.as_view()),
    path('done/personal/', DonePersonAPIView.as_view()),
    # done은 사용자가 올린 todo 전체를 보이게 하자 <int:pk>

    #path('', todolist, name='list'),   
    #path('create/', todocreate, name='create'),
    #path('update/<str:pk>/', todoupdate, name='update'),
    #path('delete/<str:pk>/', tododelete, name='delete')
]
