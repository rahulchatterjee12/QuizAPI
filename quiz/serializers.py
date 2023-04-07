from rest_framework import serializers
from .models import Quiz ,Question ,QuizAttempt

class QuizSerializer(serializers.Serializer):
    
    class Meta:
        model=Quiz
        fields = '__all__'

class QuestionSerializer(serializers.Serializer):
    
    class Meta:
        model = Question
        fields = '__all__'


class QuizAttemptSerializer(serializers.Serializer):
    
    class Meta:
        model = QuizAttempt
        fields = '__all__'