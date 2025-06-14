from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "board"
urlpatterns = [
    path("", views.board_and_task, name="board_and_task"),
    path("task_delete/", views.displayBoard, name="displayBoard"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)