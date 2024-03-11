from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length = 100)
    employee_id = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 10)
    address = models.CharField(max_length = 100)
    working = models.BooleanField(default = True)
    department = models.CharField(max_length = 10)
    image = models.ImageField(upload_to="employee/")

    def __str__(self):
        return self.employee_name

class Testimonial(models.Model):
    name = models.CharField(max_length = 200)
    testimonial = models.TextField()
    picture = models.ImageField(upload_to="testimonials/")
    rating = models.IntegerField()

    def __str__(self) -> str:
        return self.testimonial