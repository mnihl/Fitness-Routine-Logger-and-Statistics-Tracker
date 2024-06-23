from django.contrib import admin
from .models import WorkoutLog, ExerciseLog

# Register your models here.
admin.site.register(WorkoutLog)
admin.site.register(ExerciseLog)