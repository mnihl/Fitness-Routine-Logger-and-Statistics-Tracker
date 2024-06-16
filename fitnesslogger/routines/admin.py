from django.contrib import admin
from .models import Routine, Exercise

class ExerciseInline(admin.TabularInline):
    model = Exercise
    extra = 1

class RoutineAdmin(admin.ModelAdmin):
    inlines = [ExerciseInline]

# Register your models here.
admin.site.register(Routine, RoutineAdmin)
admin.site.register(Exercise)
