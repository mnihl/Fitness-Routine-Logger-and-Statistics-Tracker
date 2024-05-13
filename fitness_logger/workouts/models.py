from django.db import models

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length = 100)

class RoutineTemplate(models.Model):
    name = models.CharField(max_length = 100)
    exercises = models.ManyToManyField(Exercise, through = "RoutineExercise")

class RoutineExercise(models.Model):
    routine_template = models.ForeignKey(RoutineTemplate, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.FloatField()