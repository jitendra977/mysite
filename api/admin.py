from django.contrib import admin
from api.models import Company, Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_name','address','working')
# Register your models here.
admin.site.register(Company)
admin.site.register(Employee,EmployeeAdmin)