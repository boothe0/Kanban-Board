from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
# Create your views here.

def board(request):
    return render(request, "board/board.html")

def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                due_date = form.cleaned_data['due_date'],
                user_on_task = form.cleaned_data['user_on_task'],
            )
            print(request.user)
            task.user = request.user
            task.save()
            
    else:
        form = TaskForm()
    return render(request, 'board/task.html', {'form': form})


def displayBoard(request):
    # check for user
    pass