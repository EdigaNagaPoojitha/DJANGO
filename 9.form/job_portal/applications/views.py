from django.shortcuts import render,redirect
from .forms import Jobapplicatinform,contactForm
from django.contrib import messages
# Create your views here.
def job_application_view(request):
    form=Jobapplicatinform()
    if request.method =='POST':
        form=Jobapplicatinform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Your APPLICATION SUBMITTED SUCCESSFULLY')
            return redirect('job_application')
    return render(request,'applications/job_application.html',{'form':form})
def contact_view(request):
    form=contactForm()
    if request.method =='POST':
        form=contactForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'your message sent successfully')
            return redirect('contact')
    return render(request,'applications/contact.html',{'form':form})