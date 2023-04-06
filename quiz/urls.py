from django.urls import path
from .views import QuizList, QuizDetail, QuestionList, QuestionDetail, QuizQuestionList, QuizQuestionDetail

urlpatterns = [
    path('quizzes/', QuizList.as_view()),
    path('quizzes/<int:pk>/', QuizDetail.as_view()),
    path('questions/', QuestionList.as_view()),
    path('questions/<int:pk>/', QuestionDetail.as_view()),
    path('quiz-questions/', QuizQuestionList.as_view()),
    path('quiz-questions/<int:pk>/', QuizQuestionDetail.as_view()),
]
 