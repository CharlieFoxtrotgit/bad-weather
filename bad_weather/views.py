from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from meteostat import Point, Stations, Daily
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import QueryForm, RegisterForm

# Create your views here.
def index(request):
    if request.method == 'GET':
        queryform = QueryForm()
        
        return render(request, "bad_weather/index.html", {
            'queryform': queryform
        })

    elif request.method == 'POST':
        bound_queryform = QueryForm(request.POST)

        if bound_queryform.is_valid():
            #use the form to construct a query to meteostat
            #process the weather data
            #return relevent results
            return HttpResponse("form submitted and valid")

    else:
        return redirect('index')


def register(request):
    if request.method == "POST":
        bound_register_form = RegisterForm(request.POST)
        if bound_register_form.is_valid():
            bound_register_form.save()

        else:
            return HttpResponse("invalid form")
        
        return redirect('index')

    else:
        register_form = RegisterForm()
        return render(request, "bad_weather/register.html", {
            'register_form': register_form
        })


# def login(request):
#     if request.method == "POST":
#         bound_authenticationform = AuthenticationForm(request.POST)
        
#         if bound_authenticationform.is_valid():
#             user = authenticate(request, username=bound_authenticationform.username)

#     else:
#         authenticationform = AuthenticationForm()
#         return render(request, 'bad_weather/login.html', {
#             'authenticationform': authenticationform
#         })