from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from fitnesslogger.models import UserProfile

def welcome(request):
    return render(request, "fitnesslogger/welcome.html")

def login_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, "fitnesslogger/login.html", {"form": form})

def register_view(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect("home")
        else:
            form = UserCreationForm()
    return render(request, "fitnesslogger/register.html", {"form": form})

@login_required
def userprofile(request):
    userprofile = UserProfile.objects.get(user = request.user)
    return render(request, "fitnesslogger/userprofile.html", {"userprofile": userprofile})

@login_required
def home(request):
    userprofile = UserProfile.objects.get(user = request.user)
    return render(request, "fitnesslogger/home.html", {"userprofile": userprofile})