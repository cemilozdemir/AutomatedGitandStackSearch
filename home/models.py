from django.db import models

# Create your models here.

class users(models.Model):
    loginname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    locationu = models.CharField(max_length=100)
    company =models.CharField(max_length=100)
    repos = models.CharField(max_length=100)
    gists = models.CharField(max_length=100)
    followers = models.CharField(max_length=100)
    followingu = models.CharField(max_length=100)
    htmlurl = models.CharField(max_length=100)
    class Meta:
        db_table = "users"

class stackusers(models.Model):
    stackname = models.CharField(max_length=100)
    isemployee = models.CharField(max_length=100)
    reputation = models.CharField(max_length=100)
    weeklyrepchange = models.CharField(max_length=100)
    monthlyrepchange = models.CharField(max_length=100)
    linkurl = models.CharField(max_length=100)
    class Meta:
        db_table = 'stackusers'
            