from django import forms
from .models import JobApplication

class contactForm(forms.Form):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Enter ur name','class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter ur email','class':'form-control'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'Enter your message','class':'form-control','rows':4})
    )
class Jobapplicatinform(forms.ModelForm):
    class Meta:
        model=JobApplication
        fields=['name','email','phone','resume','cover_letter','job_type']
        widget={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter ur name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'enter ur email'}),
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'enter ur phone number'}),
            'resume':forms.FileInput(attrs={'class':'form-control','placeholder':'select resume'}),
            'cover_letter':forms.TextInput(attrs={'class':'form-control','placeholder':'write ur cover_letter','rows':4}),
            'job_type':forms.TextInput(attrs={'class':'form-control','placeholder':'enter ur name'}),
            
        }
        def clean_phone(self):
            phone=self.clean_data.get('phone')
            if not phone.isdigit() or len(phone)<10:
                raise forms.ValidationError("enter valid phone number")
            return phone
        def clean_resume(self):
            resume = self.cleaned_data.get('resume')

            if resume:
                if resume.size > 2 * 1024 * 1024:
                    raise forms.ValidationError("File size should not exceed 2MB")
                if not resume.name.endswith(('.pdf', '.doc', '.docx')):
                    raise forms.ValidationError("Only PDF and Word Docuemnts are allowed")
            return resume
    