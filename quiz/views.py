from django.shortcuts import render , HttpResponse
from django.views import View
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Quiz
from .serializers import QuizSerializer , QuestionSerializer ,QuizAttemptSerializer


class Quiz(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Quiz.objects.all()
        serializer = QuizSerializer(queryset, many=True)
        return Response(serializer.data)
