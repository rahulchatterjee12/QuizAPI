from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'
        ordering = ['id']

    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    LIVE = 'live'
    PAST = 'past'
    UPCOMING = 'upcoming'
    STATUS_CHOICES = [
        (LIVE, 'Live'),
        (PAST, 'Past'),
        (UPCOMING, 'Upcoming'),
    ]
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=UPCOMING,
    )


class Question(models.Model):

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['id']

    text = models.TextField()
    image = models.ImageField(upload_to='question_images/', null=True, blank=True)
    quiz = models.ForeignKey(Quiz, verbose_name='quiz', on_delete=models.CASCADE)
    MCQ = 'mcq'
    OPEN_TEXT = 'open_text'
    TYPE_CHOICES = [
        (MCQ, 'MCQ'),
        (OPEN_TEXT, 'Open text'),
    ]
    type = models.CharField(
        max_length=80,
        choices=TYPE_CHOICES,
        default=OPEN_TEXT,
    )


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    sequence_number = models.PositiveIntegerField()


class UserQuiz(models.Model):

    class Meta:
        verbose_name = 'UserQuizAttempt'
        verbose_name_plural = 'UserQuizAttempts'
        ordering = ['id']

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    attempt_time = models.DateTimeField(auto_now_add=True)





