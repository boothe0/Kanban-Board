from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.http import HttpResponse, JsonResponse

# Create your views here.

def board_and_task(request):
    form = TaskForm()
    tasks = Task.objects.all()
    context = {'form' : form, 'tasks' : tasks}
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
