from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class UserModel(User):
    username = models.CharField(max_length=150)



class Quiz(models.Model):

    title = models.CharField(max_length=225,name='Title')
    start_time = models.DateTimeField(name='Start Time')
    end_time = models.DateTimeField(name='End Time')
    duration = models.IntegerField(name='Duration')

class Question(models.Model):

    TYPE = [
        (0,'MCQ'),
        (1,'Open Text')
    ]

    quiz = models.ForeignKey(Quiz, related_name='question')
    text = models.CharField(max_length=225,name='Text')
    image = models.ImageField(upload_to='static/imgs',name='Image' , blank=True , null=True)
    type = models.CharField(choices=TYPE,name='Type')
    options = models.TextField(blank=True , null=True , name='Options')

class QuizAttempt(models.Model):


