from django.contrib import admin

from employeemanagement.models import Employee, Testimonial

class EmpAdmin(admin.ModelAdmin):
    list_display=('employee_id','employee_name','phone','working','image',)
    list_editable = ('employee_name','phone','working','image',)
    search_fields = ('employee_id','employee_name','phone',)
# Register your models here.
admin.site.register(Employee,EmpAdmin)
admin.site.register(Testimonial)