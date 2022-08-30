from django.urls import path, include
from .views import InfosAPIView, InfoAPIView, UserInfoView, SubjectInfoView, UserSubjectInfoView

urlpatterns = [
    path('info/',InfosAPIView.as_view()),
    path('infos/<int:fk>/',UserInfoView.as_view()),
    path('info/<int:pk>/',InfoAPIView.as_view()),
    path('info/usersubject/<int:fk>',UserSubjectInfoView.as_view()),
    path('subjectinfo/<int:fk>/',SubjectInfoView.as_view()),
]
