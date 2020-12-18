from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
class UserInfo(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    img=models.CharField(max_length=300,default='/')
    usertype=models.CharField(max_length=8)
    def __str__(self):
        return self.username+' '+self.usertype
class Dishes(models.Model):
    serverid=models.IntegerField()
    dishname=models.CharField(max_length=20)
    price=models.IntegerField()
    img=models.CharField(max_length=300)
    def __str__(self):
        return self.serverid+' '+self.dishname
class Ordered(models.Model):
    servername=models.CharField(max_length=20)
    dishname=models.CharField(max_length=20)
    price=models.IntegerField()
    num=models.IntegerField()
    def __str__(self):
        return self.servername+' '+self.dishname