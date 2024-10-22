from django.db import models
from taggit.managers import TaggableManager
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.

class website(models.Model):
    id = models.AutoField(primary_key=True)
    views = models.PositiveIntegerField(default=0)
class creator(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    icon=models.FileField(upload_to='icons/')
    firstline=models.CharField(max_length=72)
    secondline=models.CharField(max_length=72)
    thirdline=models.CharField(max_length=72)
class exp(models.Model):
    id = models.AutoField(primary_key=True)
    position=models.CharField(max_length=150)
    company=models.CharField(max_length=150)
    startdate=models.IntegerField()
    enddate=models.CharField(max_length=50)
    location=models.CharField(max_length=150)
class skill(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=150)
    rate=models.PositiveSmallIntegerField()
class project(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=48)
    Img=models.ImageField(upload_to='Project_images/')
    description=models.TextField()
    git = models.URLField(blank=True)
    tags = TaggableManager()
class bio (models.Model):
    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(to=creator, on_delete=models.CASCADE)
    smalltxt=models.CharField(max_length=24)
    bigtxt=models.CharField(max_length=24)
    

class CustomUser(AbstractUser):
    # Override the default id field with AutoField or BigAutoField
    id = models.BigAutoField(primary_key=True)  # Use BigAutoField to match MongoDB's ObjectId size
