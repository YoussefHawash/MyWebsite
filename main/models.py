from django.db import models
from taggit.managers import TaggableManager
from django.core.validators import FileExtensionValidator
# Create your models here.

class website(models.Model):
    views = models.PositiveIntegerField(default=0)
class creator(models.Model):
    name=models.CharField(max_length=48)
    pic=models.ImageField(upload_to='user_pics/',blank=True)
    about=models.TextField(max_length=300)
    address=models.CharField(max_length=150)
    git=models.URLField()
    twitter=models.URLField()
    linkedin=models.URLField()
    email=models.CharField(max_length=72)
    phone=models.CharField(max_length=72)
    projectsdone=models.IntegerField()
    firstaboutline=models.CharField(max_length=500)

class service (models.Model):
    icon=models.FileField(upload_to='icons/')
    firstline=models.CharField(max_length=72)
    secondline=models.CharField(max_length=72)
    thirdline=models.CharField(max_length=72)
class exp(models.Model):
    position=models.CharField(max_length=150)
    company=models.CharField(max_length=150)
    startdate=models.IntegerField()
    enddate=models.CharField(max_length=50)
    location=models.CharField(max_length=150)
class skill(models.Model):
    title=models.CharField(max_length=150)
    rate=models.PositiveSmallIntegerField()
class project(models.Model):
    title=models.CharField(max_length=48)
    Img=models.ImageField(upload_to='Project_images/')
    description=models.TextField()
    git = models.URLField(blank=True)
    tags = TaggableManager()
class bio (models.Model):
    creator = models.ForeignKey(to=creator, on_delete=models.CASCADE)
    smalltxt=models.CharField(max_length=24)
    bigtxt=models.CharField(max_length=24)