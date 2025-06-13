from django import forms
from django.db import models
from django.contrib.auth.models import User

class TaskForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    due_date = forms.DateField()
    user_on_task = forms.CharField(max_length=50)
