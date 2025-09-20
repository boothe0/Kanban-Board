from django.shortcuts import render
from board.models import Category, Task

# Create your views here.

def list_view(request):
    categories = Category.objects.all()
    tasks = Task.objects.all()
    if request.method == "GET":
        return render(
            request,
            "list/index.html",
            {
                "categories": categories,
                "tasks": tasks
            }
        )
