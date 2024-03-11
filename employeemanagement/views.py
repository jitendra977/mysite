from django.shortcuts import get_object_or_404, redirect, render
from employeemanagement.form import EmployeeForm
from employeemanagement.models import Employee

# Create your views here.
def emp_home(request):
    if request.method == 'POST':
        form = Employee(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/vegapp/')  # Redirect to a success page
    else:
        form = Employee()

    queryset = Employee.objects.all()
    context = {'employee':queryset}
    
    return render(request, 'emp_home.html',context)

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/emp_home/')
    else:
        form = EmployeeForm()  # Corrected the variable name here
    return render(request, 'add_employee.html', {'form': form})

# edit item
def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    print(id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/emp_home/')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form})

# delete employee 
def delete_employee(request,id):
    employee = Employee.objects.filter(id=id).first()
    if employee:
        employee.delete()
    return redirect('emp_home')