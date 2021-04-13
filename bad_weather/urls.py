from django.urls import path
from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path('accounts/login', auth_views.LoginView.as_view(template_name='bad_weather/login.html'), name="login")
]