from django.urls import path
from . import views

app_name = "bad_weather"

urlpatterns = [
    path("", views.index, name="index")
]