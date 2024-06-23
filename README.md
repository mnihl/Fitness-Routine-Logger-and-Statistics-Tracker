# Fitness Routine Logger

## Introduction

Fitness Routine Logger is a web application that allows users to create and manage fitness routines, log their workouts, and track their progress over time. Users can compare statistics and see their improvements.

## Features

- User registration and authentication
- Create and edit fitness routines
- ~~Log workouts based on routine templates~~ Partially Finished
- ~~Track performance and adjustments for each session~~ Unfinished
- ~~Data analysis of improvements over time~~ Unfinished
- ~~Compare statistics between users~~ Unfinished

## Technologies Used

- **Python**: Core programming language
- **Django**: Web framework for user management and ORM
- **Git**: Version control

## Installation
- Navigate to /fitnesslogger/
- Create and activate a virtual environment (if desired)
- Run: pip install -r requirements.txt
- Run: python manage.py runserver

### Prerequisites

- Python 3.x
- Django 3.x
- Virtual environment (recommended)

### Setup

1. Register a new user account or login with any of the following for some existing data: 
Username: abdominal
Password: abs1234abs
Username: bicep
Password: bicep1234bicep
Username: morg (superuser)
Password: 1234
Username: tricep
Password: tricep1234tricep
2. Navigate to the view profile page
3. Create a routine, save it
4. Optionally add exercises to it
5. Back on the user profile page, you can view your created routine and it's exercises, or you can choose to log a workout for this routine

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments

Thanks to the Django community for their excellent documentation and support.

### Additional comments

This project did not go as planned, I mainly ran into issues dealing with the Database Models in Django. UserProfile, Routine, Exercise, WorkoutLog, ExerciseLog all were dependent on eachother in some way and I constantly ran into bugs, crashes, issues with something not being initialized properly or missing pieces to move forward in my project. Also when I decided to simply do pytests for the functionality I had I ran into even more issues due to not being familiar with pytest-django. 

I will continue working on this project over the summer to make it what I wanted it to be. 