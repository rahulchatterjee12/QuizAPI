from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):

    title = models.CharField(max_length=225,name='Title')
    start_time = models.DateTimeField(name='Start Time')
    end_time = models.DateTimeField(name='End Time')
    duration = models.IntegerField(name='Duration')
    
    def __str__(self):
        return self.title

class Question(models.Model):

    TYPE = [
        (0,'MCQ'),
        (1,'Open Text')
    ]

    quiz = models.ForeignKey(Quiz, related_name='question',on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=225,name='Text')
    image = models.ImageField(upload_to='static/imgs',name='Image' , blank=True , null=True)
    type = models.CharField(max_length=225,choices=TYPE,name='Type')
    options = models.TextField(max_length=225, blank=True , null=True , name='Options')

    def __str__(self):
        return self.text

class QuizAttempt(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.DO_NOTHING)
    quiz = models.ForeignKey(Quiz, related_name='quiz',on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField(name='Start Time')
    end_time = models.DateTimeField(name='End Time')

    def __str__(self):
        return self.user



