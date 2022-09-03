from .models import AddStudent
from django.forms import ModelForm ,DateField
from django import forms
from django.contrib.admin import widgets


class DateInput(forms.DateInput):
     input_type = 'date'
     


class AddStudent(ModelForm):
    class Meta:
        model = AddStudent
        fields = ['name' , 'age' , 'date_of_birth' , 'grade']
        # widgets = {
        #     'date_of_birth': forms.DateInput(format=('%d-%m-%Y'))
        # }
        widgets = {'date_of_birth':DateInput()}

