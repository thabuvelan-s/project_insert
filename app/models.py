from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length = 100, primary_key = True)
    emp_no = models.IntegerField()
    sal = models.IntegerField()
    
    def __str__(self):
        return self.emp_name
    
class Dept(models.Model):
    emp_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    dept_loc = models.CharField(max_length= 100)
    dept_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.dept_name
    
class CEO(models.Model):
    dept_name = models.ForeignKey(Dept, on_delete=models.CASCADE)
    date = models.DateField()
    MD = models.CharField(max_length = 100)
    def __str__(self):
        return self.MD