from django.contrib import admin
from django.urls import path
from .views import wish,greet,wish2

urlpatterns = [
    path("view/",wish),
    path("greet/",greet),
    path("wish/",wish2)
]