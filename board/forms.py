from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import Category, Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'user_on_task', 'category']
    
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user)

class CategoryForm(forms.ModelForm):
    user = forms.CharField(max_length=50)
    class Meta:
        model = Category
        fields = ['category', 'color']
