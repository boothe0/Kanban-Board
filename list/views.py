from django.shortcuts import render

# Create your views here.

def list_view(request):
    if request.method == "GET":
        return render(request, "list/index.html")

