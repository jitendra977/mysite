# forms.py
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name', 'employee_id', 'phone', 'address', 'working', 'department', 'image']

    def __init__(self,*args, **kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class']='form-control'
