from django import forms
from .models import Student

#Model Form
class studentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
# Django Form without model        
class EmployeeRegistration(forms.Form):
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)
    Email     = forms.EmailField(label="Enter the valid email id", max_length=50)
    Indian    = forms.BooleanField()
    Mobile    = forms.DecimalField(label="Enter the 10 digit no's")