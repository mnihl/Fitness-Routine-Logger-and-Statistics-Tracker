from django.db import models
from django.core.exceptions import ValidationError
from fitnesslogger.models import UserProfile


# Create your models here.
class Routine(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    min_sets = models.IntegerField()
    max_sets = models.IntegerField()
    min_reps = models.IntegerField()
    max_reps = models.IntegerField()

    def clean(self):
        if self.min_sets > self.max_sets:
            raise ValidationError("Minimum sets cannot be greater than maximum sets")
        if self.min_reps > self.max_reps:
            raise ValidationError("Minimum reps cannot be greater than maximum reps")
        if self.min_sets < 0 or self.max_sets < 0:
            raise ValidationError("Sets cannot be negative")
        if self.min_reps < 0 or self.max_reps < 0:
            raise ValidationError("Reps cannot be negative")
        if self.min_sets == 0 and self.min_reps == 0:
            raise ValidationError("At least one of sets or reps must be greater than 0")
    
    def __str__(self):
        return self.name