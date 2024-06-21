from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from fitnesslogger.models import UserProfile
from .models import Routine, Exercise
from .forms import RoutineForm, ExerciseForm



# Create your views here.
@login_required
def create_routine(request):
    if request.method == "POST":
        form = RoutineForm(request.POST)
        if form.is_valid():
            routine = form.save(commit=False)
            print("User:", request.user)
            print("ID:", request.user.id)
            print("User Profile:", UserProfile.objects.get(user = request.user))
            routine.user = request.user.profile
            routine.save()
            print(routine.id)
            return redirect("routines:add_exercise", routine_id=routine.id)
    else:
        routine_form = RoutineForm()
    return render(request, "routines/create_routine.html", {"routine_form": routine_form})

@login_required
def add_exercise(request, routine_id):
    routine = get_object_or_404(Routine, id=routine_id, user=request.user.profile)
    ExerciseFormSet = inlineformset_factory(Routine, Exercise, form=ExerciseForm, extra=1, can_delete=True)
    if request.method == "POST":
        formset = ExerciseFormSet(request.POST, instance = routine)
        if formset.is_valid():
            formset.save()
            return redirect("routines:add_exercise", routine_id=routine.id)
    else:
        formset = ExerciseFormSet(instance = routine)
    return render(request, "routines/add_exercise.html", {"routine": routine, "formset": formset})

@login_required
def routine_detail(request, routine_id):
    userprofile = UserProfile.objects.get(user = request.user)
    routine = Routine.objects.get(id=routine_id, user=userprofile)
    exercises = Exercise.objects.filter(routine=routine)
    return render(request, 'routines/routine_detail.html', {'routine': routine, 'exercises': exercises})