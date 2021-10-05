from django.contrib import admin
from .models import service, website,creator,project,bio,exp,skill
# Register your models here.
admin.site.register(website)
admin.site.register(creator)
admin.site.register(project)
admin.site.register(bio)
admin.site.register(exp)
admin.site.register(skill)
admin.site.register(service)

