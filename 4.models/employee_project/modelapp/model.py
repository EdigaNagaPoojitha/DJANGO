from django.db import models

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=50)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=100)
    
    def __str__(self):
        return f'Employee object witrh E-name:{self.ename}'
    