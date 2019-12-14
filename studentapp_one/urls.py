# django imports
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

# app level imports
from studentapp_one import views

urlpatterns = [
    path('func_view/', views.func_view),
    path('class_view/', views.class_view.as_view()),
]