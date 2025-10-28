from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import Category, Task

COLORS = (
    ("#ADD8E6", "Blue"),
    ("#7CA37C", "Green"),
    ("#CBC3E3", "Purple"),
    ("#ff9194", "Red"),
)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'user_on_task', 'category']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user)

class CategoryForm(forms.ModelForm):
    color = forms.ChoiceField(choices=COLORS)
    class Meta:
        model = Category
        fields = ['category', 'color']
