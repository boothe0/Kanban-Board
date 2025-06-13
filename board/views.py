from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
# Create your views here.

def board(request):
    form = TaskForm()
    return render(request, "board/board.html", {'form': form})

def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        print(request.user)
        if form.is_valid():
            task = Task(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                due_date = form.cleaned_data['due_date'],
                user_on_task = form.cleaned_data['user_on_task'],
            )
            task.user = request.user
            task.save()
            
    else:
        form = TaskForm()
    return render(request, 'board/board.html', {'form': form})


def displayBoard(request):
    # check for user
    pass