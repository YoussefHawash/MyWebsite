from django.conf import settings
from django.shortcuts import render
from .models import bio, creator, project, service, website, skill, exp
import os
from django.conf import settings
# Create your views here.

def visitsCounter(mywebsite):
        mywebsite.views += 1
        mywebsite.save()

def Home(request):
    #  mywebsite = website.objects.get(pk=1)
    #  owner = creator.objects.get(pk=1)
    #  projects = project.objects.all()
    #  services = service.objects.all()
    #  bios = {
    #     'firstbio': bio.objects.all()[0],
    #     'secondbio': bio.objects.all()[1],
    #       'thirdbio': bio.objects.all()[2]
    #      }
    #  if settings.DEBUG ==False:
    #   visitsCounter(mywebsite)
    #  context = {
    #     'views': mywebsite.views,
    #     'creator': owner,
    #     'projects': projects,
    #     'firstbio': bios['firstbio'],
    #     'secondbio': bios['secondbio'],
    #     'thirdbio': bios['thirdbio'],
    #     'services':services,
    #  }
     return render(request, 'main/home.html')


def profile(request):
    try:

     owner = creator.objects.get(pk=1)
    except:
        pass
    skills = skill.objects.order_by('-rate')
    experience = exp.objects.all()
    context = {
        'creator': owner,
        'skills': skills,
        'exp': experience

    }
    return render(request, 'main/profile.html', context)
