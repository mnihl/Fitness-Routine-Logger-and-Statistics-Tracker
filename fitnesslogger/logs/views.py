from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from fitnesslogger.models import UserProfile
from routines.models import Routine, Exercise
from routines.forms import RoutineForm, ExerciseForm
from .models import WorkoutLog, ExerciseLog
from .forms import WorkoutLogForm, WorkoutLogEntryFormSet

# Create your views here.
@login_required
def create_log(request, routine_id):
    userprofile = UserProfile.objects.get(user = request.user)
    print(isinstance(userprofile, UserProfile))
    routine = Routine.objects.get(id=routine_id, user=userprofile)
    if request.method == "POST":
        workout_form = WorkoutLogForm(request.POST)
        formset = WorkoutLogEntryFormSet(request.POST)
        if workout_form.is_valid() and formset.is_valid():
            print(isinstance(userprofile, UserProfile))
            workout = workout_form.save(commit=False)
            workout.user = userprofile
            workout.routine = routine
            workout.save()
            exercises = workout_form.save()
            for exercise in exercises:
                exercise.workout = workout
                exercise.save()
            return redirect("logs:log", log_id=workout.id)
    else:
        workout_form = WorkoutLogForm()
        formset = WorkoutLogEntryFormSet()
    return render(request, "logs/create_log.html", {"workout_form": workout_form, "routine": routine, "formset": formset})

@login_required
def log(request, log_id):
    userprofile = UserProfile.objects.get(user = request.user)
    log = WorkoutLog.objects.get(id=log_id, user=userprofile)
    exercises = log.exercises.all()
    return render(request, 'logs/log.html', {'log': log, 'exercises': exercises})