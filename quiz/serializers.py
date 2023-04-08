from rest_framework import serializers
from .models import Quiz, Question, UserQuiz



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class UserQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuiz
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    
    questions = QuestionSerializer(many=True , read_only=True)

    class Meta:
        model = Quiz
        fields = '__all__'
    