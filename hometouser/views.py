from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django import forms
from .forms import NameForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "hometouser/index.html")

def make_account(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # put into database
            user = User(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password1'])
            user.save()
            # login so the user is saved and can immediately login
            login(request, user)
            url = reverse("hometouser:home", kwargs={'display_name': user.username})
            return redirect(url)
        else:
            # form invalid — render with errors
            return render(request, "hometouser/make-account.html", {"form": form})

    else:
        form = NameForm()
        return render(request, "hometouser/make-account.html", {"form": form})

def home(response, display_name):
    context = {"display_name" : display_name}
    return render(response, "hometouser/home.html", context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                url = reverse("hometouser:home", args=[user.username])
                return redirect(url)
            else:
                url = reverse("hometouser:login")
                return redirect(url)
    else:
        form = LoginForm()
        return render(request, "hometouser/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return render(request, "hometouser/index.html")
