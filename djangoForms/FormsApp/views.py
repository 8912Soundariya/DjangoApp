from django.shortcuts import render
from django.http import HttpResponse
from .forms import studentRegistration, EmployeeRegistration

# Create your views here.
def showFormData(request):
    fm = studentRegistration()
    return render(request, 'register/stuRegistration.html', {'form': fm})
    
def showEmpForm(request):
    fm = EmployeeRegistration()
    return render(request, 'register/empRegistration.html', {'form': fm})
    