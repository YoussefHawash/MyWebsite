from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import bio, creator, project, service, website, skill, exp

# Increment website views
def visitsCounter(mywebsite):
    mywebsite.views += 1
    mywebsite.save()

# Home view
def Home(request):
    mywebsite = get_object_or_404(website, pk=1)

    owner = creator.objects.get(pk=1)
    projects = project.objects.all()
    services = service.objects.all()

    bios = bio.objects.all()
    bios_data = {
        'firstbio': bios[0] if len(bios) > 0 else None,
        'secondbio': bios[1] if len(bios) > 1 else None,
        'thirdbio': bios[2] if len(bios) > 2 else None
    }

    if not settings.DEBUG:
        if not request.session.get('has_viewed_home', False):
            visitsCounter(mywebsite)  
            request.session['has_viewed_home'] = True  

    context = {
        'views': mywebsite.views,
        'creator': owner,
        'projects': projects,
        'firstbio': bios_data['firstbio'],
        'secondbio': bios_data['secondbio'],
        'thirdbio': bios_data['thirdbio'],
        'services': services,
    }
    return render(request, 'main/home.html', context)


# def profile(request):
#     owner = None
#     try:
#         owner = creator.objects.get(pk=1)
#     except creator.DoesNotExist:
#         pass  

  
#     skills = skill.objects.order_by('-rate')  
#     experience = exp.objects.all()  

#     context = {
#         'creator': owner,
#         'skills': skills,
#         'exp': experience,
#     }
#     return render(request, 'main/profile.html', context)
