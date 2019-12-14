# restframework imports 
from rest_framework import serializers


# app level import 
from studentapp_one.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'address', 'dob', 'roll', 'marks']