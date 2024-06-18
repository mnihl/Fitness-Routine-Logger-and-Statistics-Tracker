from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'routines' 
urlpatterns = [
    path("create/", views.create_routine, name = "create_routine"),
    path("create/add_exercise/<int:routine_id>/", views.add_exercise, name = "add_exercise")
]