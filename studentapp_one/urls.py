# django imports
from django.urls import path

# app level imports
from studentapp_one import views

urlpatterns = [
    path('func_view/', views.func_view)
]