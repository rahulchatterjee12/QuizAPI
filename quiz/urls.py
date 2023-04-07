from django.contrib import admin
from django.urls import path , include
from .views import Quiz



urlpatterns = [
    path('/',Quiz.as_view(),name='quiz')
]
