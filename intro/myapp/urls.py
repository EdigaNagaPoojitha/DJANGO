from django.urls import path
from .views import display,morning,greet
urlpatterns=[
    path('app/',display,name="display"),
    path('time/',greet,name="display")
]