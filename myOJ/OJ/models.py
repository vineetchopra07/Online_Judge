from decimal import DefaultContext
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from django.utils.timezone import now
class Problem(models.Model):
    prob_name = models.CharField(max_length=100)
    prob_desc = models.CharField(max_length=10000)
    prob_diff = models.CharField(max_length=50)
    score = models.FloatField(default=0) 

    def __str__(self):
        return self.prob_name 

class Test_cases(models.Model):
    probId = models.ForeignKey(Problem,on_delete=models.CASCADE)
    input = models.CharField(max_length=10000)
    output = models.CharField(max_length=10000)

    def __str__(self):
        return self.input

class Submission(models.Model):
    user_Id = models.ForeignKey(User,on_delete=models.CASCADE)
    probId = models.ForeignKey(Problem,on_delete=models.CASCADE)
    timestrap = models.DateTimeField(default=now)
    verdict = models.CharField(max_length=10,default='NOT SOLVED')

class User_score(models.Model):
    user_Id = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    score = models.FloatField(default=0)

