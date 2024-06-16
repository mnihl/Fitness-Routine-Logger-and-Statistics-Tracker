from django import forms
from .models import Routine, Exercise

class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'description']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'min_sets', 'max_sets', 'min_reps', 'max_reps']