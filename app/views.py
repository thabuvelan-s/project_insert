from django.shortcuts import render

# Create your views here.
from app.models import *

def insert_emp(request):
    ELOB = Employee.objects.all()
    d = {'ELOB': ELOB}
    return render(request,'emp.html',d)

def insert_dept(request):
    DLOB = Dept.objects.all()
    d = {'DLOB':DLOB}
    return render(request,'dept.html',d)

def insert_ceo(request):
    CLOB = CEO.objects.all()
    d = {'CLOB':CLOB}
    return render(request,'ceo.html',d)