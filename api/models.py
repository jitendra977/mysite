from django.db import models


# Creating a company modal
class Company(models.Model):
    name = models.CharField(max_length=50)
    company_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length =50)
    about = models.TextField()
    type = models.CharField(max_length = 100,choices=(('IT','IT'),('AUTOMOBILE','AUTOMOBILE'),('ELECTRICAL','ELECTRICAL')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length = 100)
    employee_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length = 10)
    address = models.CharField(max_length = 100)
    working = models.BooleanField(default = True)
    position = models.CharField(max_length = 20,choices=(('Manager','Manager'),('Cashier','Cashier'),('Software Developer','Software Developer'),('Project Manager','Project Manager')))
    image = models.ImageField(upload_to="employee/")
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name