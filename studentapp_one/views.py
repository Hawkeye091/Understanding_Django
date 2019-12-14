# python imports
import json

# django level imports
from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

# rest_framework imports
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# app level imports 
from studentapp_one.serializers import StudentSerializer
from studentapp_one.models import Student
from studentapp_one.serializers import TeacherSerializer
from studentapp_one.models import Teacher

# Create your views here.
@csrf_exempt 
def func_view(request):
    """
    A function based view
    """
    if request.method == "GET":
        return HttpResponse("Function based")
    if request.method == "POST":
        return HttpResponse(request.body)


class class_view(View):
    """
    A class based view
    """

    def get(self, request):
        return HttpResponse("Class based")

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(methods=['GET', 'POST'], detail=False, url_path="good_students")
    def good_students(self, request):
        good_students = Student.objects.filter(marks__maths__gte=70)
        serializer = StudentSerializer(good_students, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
        


class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    @action(methods=['POST'], detail=False, url_path="post_teacher")
    def post_teacher(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            Teacher.objects.create(
                name=validated_data['name'],
                address=validated_data['address'],
                department=validated_data['department'],
                salary=validated_data['salary'],
            )
            return HttpResponse(validated_data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['PUT'], detail=True, url_path="update_teacher_salary")
    def update_teacher_salary(self, request, *args, **kwargs):
        filter_kwargs = {self.lookup_field : self.kwargs[self.lookup_field]}
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            To_update = Teacher.objects.get(**filter_kwargs)
            To_update.salary = validated_data['salary']
            To_update.save()
            return Response(validated_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)