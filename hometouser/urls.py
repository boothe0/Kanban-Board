from django.urls import path
from . import views

app_name = "hometouser"
urlpatterns = [
    path("", views.index, name="index"),
    path("make-account/", views.make_account, name="make_account"),
    path("<str:display_name>/welcome/", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("logged-out/", views.logout_view, name="logout" )
]