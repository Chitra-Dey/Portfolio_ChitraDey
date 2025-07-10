from django.contrib import admin
from .models import Contact,Project,Skill
# Register your models here.

#user-wadmin

admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Skill)