from django.shortcuts import render,redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
# Create your views here.
#FUNCTION BASED VIEWW
def contact_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            send_mail(
                subject=f'New Contact message',
                 message=f"Sender: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.EMAIL_HOST_USER,   # sender (your Gmail)
                recipient_list=['ediganagapoojitha@gmail.com'],  # receiver (admin)
                fail_silently=False,
            )
            return redirect('contact')
    else:
        form=ContactForm()
    return render(request,'contact.html',{'form':form})
# CLASS BASE VIEW
# class contact_view(FormView):
#     template_name='contact.html'
#     form_class=ContactForm
#     success_url=reverse_lazy('contact')
#     def form_valid(self, form):
#         return super().form_valid(form)
    
    
