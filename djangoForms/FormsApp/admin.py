from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'contact', 'email', 'age','file')
