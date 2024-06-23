from django import forms
from .models import WorkoutLog, ExerciseLog
from django.forms import inlineformset_factory, formset_factory

class WorkoutLogForm(forms.ModelForm):
    class Meta:
        model = WorkoutLog
        fields = []

WorkoutLogEntryFormSet = inlineformset_factory(WorkoutLog, ExerciseLog, fields=('exercise', 'sets', 'reps', 'weight', 'completed'), extra=0)


