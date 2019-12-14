# python imports
import json

# django level imports
from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt


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
