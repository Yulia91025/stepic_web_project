from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager() 
    title = models.CharField(default='', max_length = 1024)
    text = models.TextField(default='')
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name="q_to_u")
    likes = models.ManyToManyField(User, related_name="q_to_l")

    def __unicode__(self):
        return self.title
    
    def get_url(self):
        return '/question/{}/'.format(self.id)

class Answer(models.Model):
    text = models.TextField(default='')
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name="a_to_q")
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name="a_to_u")

    def __unicode__(self):
        return self.text