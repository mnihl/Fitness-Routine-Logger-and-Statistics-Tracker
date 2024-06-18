from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from .models import Routine, Exercise
from .forms import RoutineForm, ExerciseForm



# Create your views here.
def create_routine(request):
    if request.method == "POST":
        form = RoutineForm(request.POST)
        if form.is_valid():
            routine = form.save()
            print(routine.id)
            return redirect("routines:add_exercise", routine_id=routine.id)
    else:
        routine_form = RoutineForm()
    return render(request, "routines/create_routine.html", {"routine_form": routine_form})

def add_exercise(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id)
    ExerciseFormSet = inlineformset_factory(Routine, Exercise, form=ExerciseForm, extra=1)
    if request.method == "POST":
        formset = ExerciseFormSet(request.POST, instance = routine)
        if formset.is_valid():
            formset.save()
            return redirect("routines:add_exercise", routine_id=routine.id)
    else:
        formset = ExerciseFormSet(instance = routine)
    return render(request, "routines/add_exercise.html", {"routine": routine, "formset": formset})