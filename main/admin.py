from django.contrib import admin
from .models import creator, website, service, exp, skill, project, bio

@admin.register(creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')  # Explicitly show the ID field

@admin.register(website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'views')

@admin.register(service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstline', 'secondline', 'thirdline')

@admin.register(exp)
class ExpAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'company', 'startdate', 'enddate')

@admin.register(skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rate')

@admin.register(project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'git')

@admin.register(bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('id', 'smalltxt', 'bigtxt', 'creator')
