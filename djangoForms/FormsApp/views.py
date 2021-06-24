from django.shortcuts import render
from django.http import HttpResponse
from .forms import studentRegistration, EmployeeRegistration

# Create your views here.
def showFormData(request):
    fm = studentRegistration()
    return render(request, 'register/stuRegistration.html', {'form': fm})
    
def showEmpForm(request):
    if request.method == 'POST':
        fm = EmployeeRegistration(request.POST)
        if fm.is_valid():
            Firstname = fm.cleaned_data['firstname']
            lastname = fm.cleaned_data['lastname']
            Email = fm.cleaned_data['Email']
            Indian =  fm.cleaned_data['Indian']
            Mobile = fm.cleaned_data['Mobile']
            
            print('Name: ', Firstname + lastname)
            print('Email Id: ', Email)
            print('Are you indian? : ', Indian)
            print('Contact No.', Mobile)
    else:
        fm = EmployeeRegistration()
        print('Hitted the GET request')
    return render(request, 'register/empRegistration.html', {'form': fm})
    