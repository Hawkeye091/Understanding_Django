from django.shortcuts import render, HttpResponse

# Create your views here.
def func_view(request):
    return HttpResponse("Hello")