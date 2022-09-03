from django.urls import path, include
from .views import UserSubjectView,UsersSubjectView,UserEditView

urlpatterns = [
    path('usersubject/',UsersSubjectView.as_view()), # 모든 유저의 유저과목
    path('usersubject/<int:fk>',UserSubjectView.as_view()), # 유저별 과목리스트, fk= user_id
    path('usersubject/<int:fk>/<int:pk>',UserEditView.as_view()) # 상세조회
]