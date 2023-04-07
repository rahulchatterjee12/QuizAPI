from django.urls import path 
from .views import Quiz
from rest_framework import routers


urlpatterns = [
    path('',Quiz.as_view({'get':'list'}),name='quiz')
]
