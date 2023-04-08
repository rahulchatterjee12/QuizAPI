from django.urls import path
from .views import QuizList, QuizDetail

urlpatterns = [
    path('quizzes/', QuizList.as_view()),
    path('quizzes/<int:pk>/', QuizDetail.as_view()),
]
 