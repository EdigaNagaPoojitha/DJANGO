# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.utils import timezone
def display(request):
    s="<h1> HELLO,POOOOOOJI</h1>"
    return HttpResponse(s)
def morning(request):
    time=datetime.datetime.now()
    return HttpResponse(time)
def greet(request):
    current_time=timezone.now()
    hour=current_time.hour
    if 6<=hour<=12:
        greeting_message="good morning"
    elif 12<=hour<=16:
        greeting_message="good afternoon"
    else:
        greeting_message="good nyt"
    time=current_time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse(f"{greeting_message} frndsss,wake up it'S {time}  now..........")
    