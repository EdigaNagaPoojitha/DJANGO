from django.contrib import admin

# Register your models here.
from .model import Employee
class Employeeadmin(admin.ModelAdmin):
    list_display=['eno','ename','eaddr','esal']
admin.site.register(Employee)