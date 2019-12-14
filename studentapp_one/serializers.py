# restframework imports 
from rest_framework import serializers


# app level import 
from studentapp_one.models import Student, Teacher

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'address', 'dob', 'roll', 'marks']

class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    department = serializers.CharField(required=False)
    salary = serializers.FloatField(required=False)

    def validate(self, data):
        name = data.get('name', None)
        address = data.get('address', None)
        department = data.get('department', None)
        salary = data.get('salary', None)

        return {
            "name": name, "address": address,
            "department": department, "salary": salary,
        }
