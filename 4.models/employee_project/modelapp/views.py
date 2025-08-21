from django.shortcuts import render
from .model import Employee
# Create your views here.
def Employee_view(request):
    Emp_data=Employee.objects.all()
    my_dic={'emp_data':Emp_data}
    return render(request,'myapp/home.html',context=my_dic)