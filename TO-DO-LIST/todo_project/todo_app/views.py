from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import Registerform,Loginform,ProfileForm
from .models import Task

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        user_form = Registerform(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()  # Save User
            profile = profile_form.save(commit=False)
            profile.user = user      # Link profile to user
            profile.save()
            return redirect('login')
    else:
        user_form = Registerform()
        profile_form = ProfileForm()
    return render(request, 'todo_app/register.html', {'user_form': user_form, 'profile_form': profile_form})

def login_view(request):
    if request.method == 'POST':
        form=Loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('dashboard')
    else:
        form=Loginform()
    return render(request,'todo_app/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return('login')

def dashboard(request):
    tasks=Task.objects.filter(user=request.user)
    return render(request,'todo_app/dashboard.html',{'tasks':tasks})