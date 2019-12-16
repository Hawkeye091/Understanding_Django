from django.contrib import admin

# Register your models here.

# App level imports
from studentapp_one.models import Student, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'dob', 'roll', 'marks']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'department', 'salary']
