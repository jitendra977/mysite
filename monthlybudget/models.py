from django.db import models

class Transactions(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length = 200)
    CATEGORY_CHOICES = (
        ('Personal', 'Personal'),
        ('Food', 'Food'),
        ('Health', 'Health'),
        ('Transportation', 'Transportation'),
        ('Clothes', 'Clothes'),
    )
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    PAYMENT_CHOICES = (
        ('PayPal', 'PayPal'),
        ('Credit', 'Credit'),
        ('Cash', 'Cash'),
        ('Copen', 'Copen'),
    )
    payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES)

    
    def __str__(self):
        return self.description
    