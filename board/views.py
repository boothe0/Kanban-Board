from django.shortcuts import render, redirect
from .forms import TaskForm, CategoryForm
from .models import Task, Category
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def board_and_task(request):
    if request.method == 'POST':
        if 'submitTask' in request.POST:
            taskForm = TaskForm(request.POST, prefix='task')
            categoryForm = CategoryForm(prefix='category')
            if taskForm.is_valid():
                task = Task(
                    name = taskForm.cleaned_data['name'],
                    description = taskForm.cleaned_data['description'],
                    due_date = taskForm.cleaned_data['due_date'],
                    user_on_task = taskForm.cleaned_data['user_on_task'],
                    category = taskForm.cleaned_data['category']
                )
                task.user = request.user
                task.save()
            
        elif 'submitCategory' in request.POST:
            categoryForm = CategoryForm(request.POST, prefix='category')
            taskForm = TaskForm(prefix='task')
            if categoryForm.is_valid():
                username = categoryForm.cleaned_data['user']
                try:
                    userCreatedCat = User.objects.get(username = username)
                except User.DoesNotExist:
                    messages.error(request, "Try a different user")
                    return redirect('board:board_and_task')
                category = Category(
                    category = categoryForm.cleaned_data['category'],
                    color = categoryForm.cleaned_data['color'],
                    user = userCreatedCat
                )
                
                category.save()
    else:
        # only make the empty forms once rather than at the top
        taskForm = TaskForm(prefix="task")
        categoryForm = CategoryForm(prefix="category")
    # pass these in for use in html
    categories = Category.objects.all()
    tasks = Task.objects.all()
    context = {'taskForm' : taskForm, 'categoryForm' : categoryForm, 'tasks' : tasks, 'categories' : categories}

    return render(request, "board/board.html", context)

def displayBoard(request):
    # if there is a get request to task_delete/ 
    if request.method == "GET":
        # gets id of the data passed in from js
        task_id = request.GET.get("task_to_delete")
        if task_id:
            try:
                task = Task.objects.get(pk=task_id)
                task.delete()
                # triggers success in js 
                return JsonResponse({"status" : "success"})
            except Task.DoesNotExist:
                # the rest trigger errors in js
                return JsonResponse({"status": "error", "message": "Task not found"}, status=404)
        else:
            return JsonResponse({"status": "error", "message": "No task id provided"}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
