from django.urls import path, include
from .views import SubjectsAPIView,SubjectAPIView

urlpatterns = [
    path('subject/', SubjectsAPIView.as_view()),
    path('subject/<int:pk>',SubjectAPIView.as_view())
] 
