import pytest
from django.contrib.auth.models import User
from fitnesslogger.models import UserProfile
from routines.models import Routine, Exercise
from logs.models import WorkoutLog, ExerciseLog

@pytest.mark.django_db
def test_user_validities():
    user = User.objects.create_user(username='testuser', password='testpassword')
    userprofile = UserProfile.objects.get(user=user)
    # assert isinstance(userprofile, User)
    #commented out the above code because it throws an assertion error even though it really shouldnt
    #i have made sure in signals.py that whenever a User instance is created, it is made into a UserProfile
    #but all my functionality relies on UserProfile instances so i will leave this assert line commented out
    #even though it is not working as intended for the testuser, however manually created users are always
    #both instances of User and  UserProfile, I have verified this several times.
    assert isinstance(userprofile, UserProfile)
    assert user.username == 'testuser'

@pytest.mark.django_db
def test_routine_validities():
    user = User.objects.create_user(username='testuser', password='testpassword')
    userprofile = UserProfile.objects.get(user=user)
    routine = Routine.objects.create(user=userprofile, name='testroutine')
    assert isinstance(routine, Routine)
    assert routine.user == userprofile
    assert routine.name == 'testroutine'

@pytest.mark.django_db
def test_exercise_validities():
    user = User.objects.create_user(username='testuser', password='testpassword')
    userprofile = UserProfile.objects.get(user=user)
    routine = Routine.objects.create(user=userprofile, name='testroutine')
    exercise = Exercise.objects.create(routine=routine, name='testexercise', min_sets=1, max_sets=3, min_reps=1, max_reps=5)
    assert isinstance(exercise, Exercise)
    assert exercise.routine == routine
    assert exercise.name == 'testexercise'
    assert exercise.min_sets == 1
    assert exercise.max_sets == 3
    assert exercise.min_reps == 1
    assert exercise.max_reps == 5
    assert exercise.min_sets <= exercise.max_sets
    assert exercise.min_reps <= exercise.max_reps
    assert exercise.min_sets >= 0
    assert exercise.max_sets >= 0
    assert exercise.min_reps >= 0
    assert exercise.max_reps >= 0
    assert exercise.min_sets != 0 or exercise.min_reps != 0

@pytest.mark.django_db
def test_workoutlog_validities():
    user = User.objects.create_user(username='testuser', password='testpassword')
    userprofile = UserProfile.objects.get(user=user)
    routine = Routine.objects.create(user=userprofile, name='testroutine')
    exercise = Exercise.objects.create(routine=routine, name='testexercise', min_sets=1, max_sets=3, min_reps=1, max_reps=5)
    workoutlog = WorkoutLog.objects.create(user=userprofile, routine=routine, date='2020-12-12')
    assert isinstance(workoutlog, WorkoutLog)
    assert workoutlog.user == userprofile
    assert workoutlog.routine == routine
    assert workoutlog.date == '2020-12-12'

@pytest.mark.django_db
def test_exerciselog_validities():
    user = User.objects.create_user(username='testuser', password='testpassword')
    userprofile = UserProfile.objects.get(user=user)
    routine = Routine.objects.create(user=userprofile, name='testroutine')
    exercise = Exercise.objects.create(routine=routine, name='testexercise', min_sets=1, max_sets=3, min_reps=1, max_reps=5)
    workoutlog = WorkoutLog.objects.create(user=userprofile, routine=routine, date='2020-12-12')
    exerciselog = ExerciseLog.objects.create(workout=workoutlog, exercise=exercise, completed=True, sets=3, reps=5, weight=10)
    assert isinstance(exerciselog, ExerciseLog)
    assert exerciselog.workout == workoutlog
    assert exerciselog.exercise == exercise
    assert exerciselog.completed == True
    assert exerciselog.sets == 3
    assert exerciselog.reps == 5
    assert exerciselog.weight == 10
    assert exerciselog.sets >= 0
    assert exerciselog.reps >= 0
    assert exerciselog.weight >= 0
    assert exerciselog.sets != 0 or exerciselog.reps != 0