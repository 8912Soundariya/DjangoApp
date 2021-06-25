from django import forms
from .models import Student

#Model Form
class studentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'first_name': 'Enter your first name here',
            'last_name': 'Enter your last name here',
            'email': 'Enter valid email id'
        }
        help_text = {'last_name': 'Enter your full surname'}
        error_messages = {
            'age': {'required':'Enter your right age','max_length':'Age max_length is 2 digit'},
            'first_name': {'required':'Name is Mandatory'}
        }
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'nameFirst','placeholder':'Name please...'}),
            'last_name':forms.TextInput()
        }
        
# Django Form without model        
class EmployeeRegistration(forms.Form):
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)
    Email     = forms.EmailField(label="Enter the valid email id", max_length=50)
    Indian    = forms.BooleanField()
    Mobile    = forms.DecimalField(label="Enter the 10 digit no's")
    File      = forms.FileField() # for creating file input 