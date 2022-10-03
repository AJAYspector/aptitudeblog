from distutils.command.upload import upload
from secrets import choice
from unicodedata import name
from django.db import models
from django.forms import CharField

# Create your models here.
class Fun(models.Model):
    quest=models.TextField()
    choi1 = models.TextField()
    choi2 = models.TextField()
    choi3 = models.TextField()
    choi4 = models.TextField()
    ans = models.TextField()
    exp=models.TextField()

class data(models.Model):
    name=models.CharField(max_length=70)
    score=models.IntegerField()
    at=models.IntegerField()
    uphoto=models.ImageField(upload_to='pics')

class maths(models.Model):
    quest=models.TextField()
    choi1 = models.TextField()
    choi2 = models.TextField()
    choi3 = models.TextField()
    choi4 = models.TextField()
    ans = models.TextField()
    exp=models.TextField()