from django import forms
from django.contrib.auth.models import User
from  django.contrib.auth.forms import UserCreationForm
from .models import Profile

class Registerform(UserCreationForm):
    email=forms.EmailField
    
    class Meta:
        model:User
        fields=['username','email','password1','password2']
        
class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'profile_pic']