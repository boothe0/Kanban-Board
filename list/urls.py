from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "list"
urlpatterns = [
    path("", views.list_view, name="list_view"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)