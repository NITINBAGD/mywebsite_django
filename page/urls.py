# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("" , views.page , name="page"),
    # path("register" ,views.register , name = "register"),
  
]