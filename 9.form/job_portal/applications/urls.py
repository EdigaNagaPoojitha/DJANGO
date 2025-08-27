from django.urls import path
from .views import contact_view,job_application_view
urlpatterns=[
    path('apply/',job_application_view,name='job_application'),
    path('contact/',contact_view,name='contact')
]