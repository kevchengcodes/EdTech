from django.contrib import admin
from .models import Projects, StudentLevel, SubjectList

# Register your models here.
admin.site.register(Projects)
admin.site.register(StudentLevel)
admin.site.register(SubjectList)