from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from meteostat import Point, Stations, Daily

from .forms import QueryForm

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
