from django.urls import path,include
from .views import Employee_view
urlpatterns = [
    path("data/",Employee_view,name="employee")
]