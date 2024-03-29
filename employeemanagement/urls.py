

from django.urls import path

from employeemanagement.views import add_employee, delete_employee, emp_home, update_employee


urlpatterns = [
    path('',emp_home,name ='emp_home'),
    path('emp_home/',emp_home,name ='emp_home'),
    path('add_employee/',add_employee,name ='add_employee'),
    path('update_employee/<int:id>/', update_employee, name='update_employee'),
    path('delete_employee/<int:id>/', delete_employee, name='delete_employee'),
]
   
   