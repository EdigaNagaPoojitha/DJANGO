from django.shortcuts import render
from .models import Department,Employee
from django.db.models import Avg,Count,Sum
from django.db import connection
# Create your views here.
def all_employees(request):
    employees=Employee.objects.all()
    return render(request,'employees/all.html',{'employees':employees})
def it_department_employees(request):
    it_employees=Employee.objects.filter(department__name='IT')
    return render(request,'employees/it_department_employees.html',{'it_employees':it_employees})
def high_salary_employees(request):
    high_salary_employees=Employee.objects.filter(salary__gt=55000)
    return render(request,'employees/high_salary_employees.html',{'high_salary_employees':high_salary_employees})
def avg_salary_per_department(request):
    avg_salary_per_department=Employee.objects.annotate(avg_salary=Avg('salary'))
    return render(request,'employees/avg_salary_per_department.html',{'avg_salary_per_department':avg_salary_per_department})
def avg_salary(request):
    avg_salary=Employee.objects.aggregate(avg_salary=Avg('salary'))
    return render(request,'employees/avg_salary_per_department.html',{'avg_salary=':avg_salary})

def department_with_most_employees(request):
    department = Department.objects.annotate(num_employees=Count('employee')).order_by('-num_employees').first()
    return render(request, 'employees/department_with_most_employees.html', {'department': department})

def high_paid_employees(request):
    # ORM query — fully safe, no raw SQL needed
    employees = Employee.objects.filter(salary__gt=60000)
    return render(request, 'employees/high_salary_employees.html', {'employees': employees})
