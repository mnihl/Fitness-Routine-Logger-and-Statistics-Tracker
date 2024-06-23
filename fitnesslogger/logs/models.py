from django.db import models
from fitnesslogger.models import UserProfile
from routines.models import Routine, Exercise


# Create your models here.
class WorkoutLog(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default = 1)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField(blank = True, null = True)
    duration = models.DurationField(blank = True, null = True)
    exercises = models.ManyToManyField(Exercise, through='ExerciseLog')
    def __str__(self):
        return f"{self.user.username}'s {self.routine.name} on {self.date}"

class ExerciseLog(models.Model):
    workout = models.ForeignKey(WorkoutLog, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    sets = models.IntegerField(blank = True, null = True)
    reps = models.IntegerField(blank = True, null = True)
    weight = models.FloatField(blank = True, null = True)
    notes = models.TextField(blank = True, null = True)
    def __str__(self):
        return f"{self.exercise.name} in {self.workout}"