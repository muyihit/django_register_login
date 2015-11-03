#coding=utf8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    userID = models.IntegerField()
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length = 16, null = True, default = '')
    age = models.IntegerField()
    sex = models.IntegerField()
    phone = models.CharField(max_length = 20)
    qq = models.CharField(max_length = 20)
    home = models.CharField(max_length = 50)
    goal = models.CharField(max_length = 50)
    date = models.DateField()
    price = models.IntegerField()
    number = models.IntegerField()
    busy = models.IntegerField()
    tip = models.CharField(max_length = 128, null = True, default = '')
    question = models.CharField(max_length = 128, null = True, default = '')
    answer = models.CharField(max_length = 128, null = True, default = '')

    def __unicode__(self):
        return self.user.username
    
class Site(models.Model):
    siteID = models.IntegerField()
    name = models.CharField(max_length = 20)
    price = models.IntegerField()

class Log(models.Model):
    logID = models.IntegerField()
    user = models.ForeignKey(User)
    title = models.CharField(max_length = 50)
    content = models.CharField(max_length = 1000)
    site = models.OneToOneField(Site)
    date = models.DateField()

class Strategy(models.Model):
    strategyID = models.IntegerField()
    user = models.ForeignKey(User)
    title = models.CharField(max_length = 50)
    content = models.CharField(max_length = 1000)
    date = models.DateField()


    
 
