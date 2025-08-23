from django.shortcuts import render
from django.views.generic import ListView
from .models import Employee_proxy,Customer_proxy

class EmployeeListView(ListView):
    model=Employee_proxy
    template_name='people/employee_list.html'
    context_object_name='employees'
class CustomerListView(ListView):
    model=Customer_proxy
    template_name='people/customers_list.html'
    context_object_name='customers'
    
