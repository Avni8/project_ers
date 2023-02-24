from django import forms
from .models import Employee

class EmployeeCreateForm(forms.ModelForm):
    """ Form Class for Employee Creation """
    class Meta:
        fields = "__all__" #to create form including all fields
        # fields = ("full_name", "contact",)  #to create form containing only fullname and contact fields
        model =  Employee
