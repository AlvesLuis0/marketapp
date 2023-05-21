from django.urls import path

from . import views

urlpatterns = [
  path("", views.clientView, name="index"),
  path("login/", views.login, name="login"),
  path("register/", views.register, name="register"),
  path("client", views.createClient, name="createClient")
]