from django.contrib import admin
from django.urls import path, include
from routines import views


urlpatterns = [
    path("create/", views.create_routine, name = "create_routine"),
]