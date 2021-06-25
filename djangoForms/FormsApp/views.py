from django.shortcuts import render
from django.http import HttpResponse
from .forms import studentRegistration, EmployeeRegistration
from FormsApp.functions import handle_uploaded_file 
from .models import Student

# Create your views here.
def showFormData(request):
    if request.method == 'POST':
        fm = studentRegistration(request.POST,request.FILES)
        if fm.is_valid():
            Firstname = fm.cleaned_data['first_name']
            Lastname = fm.cleaned_data['last_name']
            Contact = fm.cleaned_data['contact']
            Email =  fm.cleaned_data['email']
            Age = fm.cleaned_data['age']
            File = handle_uploaded_file(request.FILES['file']) # Its storing data in the local dir
            File = fm.cleaned_data['file'] # Its storing file name in the DB directly
            reg = Student(first_name=Firstname,last_name=Lastname,contact=Contact,email=Email,age=Age,file=File)
            reg.save()
            # reg = Student(id=2,first_name=Firstname,last_name=Lastname,contact=Contact,email=Email,age=Age) # Update record which id is 2
            # reg.save()
            # reg = Student(id=5) # Delete the record from DB which id is 5
            # reg.delete()
            
            print('Name: ', Firstname + Lastname)
            print('Email Id: ', Email)
            print('Age : ', Age)
            print('Contact No.', Contact)
            fm = studentRegistration() # Clear the form
    else:
        fm = studentRegistration()
    return render(request, 'register/stuRegistration.html', {'form': fm})
    
def showEmpForm(request):
    if request.method == 'POST':
        fm = EmployeeRegistration(request.POST,request.FILES)
        if fm.is_valid():
            Firstname = fm.cleaned_data['firstname']
            lastname = fm.cleaned_data['lastname']
            Email = fm.cleaned_data['Email']
            Indian =  fm.cleaned_data['Indian']
            Mobile = fm.cleaned_data['Mobile']
            File = handle_uploaded_file(request.FILES['File'])
            File = fm.cleaned_data['File']
            
            print('Name: ', Firstname + lastname)
            print('Email Id: ', Email)
            print('Are you indian? : ', Indian)
            print('Contact No.', Mobile)
            print('Uploaded filename: ', File)
            fm = EmployeeRegistration() # Clear the form
    else:
        fm = EmployeeRegistration()
        print('Hitted the GET request')
    return render(request, 'register/empRegistration.html', {'form': fm})
    