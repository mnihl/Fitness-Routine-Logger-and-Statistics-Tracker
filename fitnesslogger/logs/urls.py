from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'logs' 
urlpatterns = [
    path("create/<int:routine_id>/", views.create_log, name = "create_log"),
    path("log/<int:log_id>", views.log, name = "log"),
    # path("edit/<int:log_id>", views.edit_log, name = "edit_log"),
]

