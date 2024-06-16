from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import Routine, Exercise
from .forms import RoutineForm, ExerciseForm



# Create your views here.
def create_routine(request):
    ExerciseFormSet = inlineformset_factory(Routine, Exercise, fields=('name', 'min_sets', 'max_sets', 'min_reps', 'max_reps'))
    if request.method == "POST":
        form = RoutineForm(request.POST)
        formset = ExerciseFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            routine = form.save()
            exercises = formset.save(commit=False)
            for exercise in exercises:
                exercise.routine = routine
                exercise.save()
            return redirect("profile")
    else:
        form = RoutineForm()
        formset = ExerciseFormSet()
    return render(request, "routines/create_routine.html", {"form": form, "formset": formset})