from django.shortcuts import render

# Create your views here.
import datetime
from django.utils import timezone
def wish(request):
    time=datetime.datetime.now()
    name="ABC"
    rollno=101
    marks=90
    formatted_time=time.strftime("%d-%m-%Y %H:%M:%S")
    my_dict={
        "insert_date":formatted_time,
        "NAME":name,
        "ROLLNO":rollno,
        "MARKS":marks,
    }
    return render (request,"wish.html",my_dict)
def greet(request):
    current_time=timezone.now()
    hour=current_time.hour
    greeting_message="HELLOOO FRIENDSS!!!!!!! VERY "
    if 6<=hour<=12:
        greeting_message+="good morning...."
    elif 12<=hour<=16:
        greeting_message+="good afternoon......"
    else:
        greeting_message+="good nyt...."
    time=current_time.strftime("%d-%m-%Y %H:%M:%S")
    mydict={"insert_time":time,"insert_data":greeting_message}
    return render(request,"wish.html",context=mydict)
def wish2(request):
    current_time=timezone.now()
    hour=current_time.hour
    current_time=timezone.now()
    hour=current_time.hour
    greeting_message="HELLOOO FRIENDSS!!!!!!! VERY "
    if 6<=hour<=12:
        greeting_message+="good morning...."
    elif 12<=hour<=16:
        greeting_message+="good afternoon......"
    else:
        greeting_message+="good nyt...."
    time=current_time.strftime("%d-%m-%Y %H:%M:%S")
    return render(request,"greet.html",{"insert_time":time,"msg":greeting_message})