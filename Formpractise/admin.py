from django.contrib import admin
from .models import Student
# Register your models here.
class Studentadmin(admin.ModelAdmin):
    pass

admin.site.register(Student, Studentadmin)