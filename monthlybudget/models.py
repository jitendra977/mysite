from django.db import models

class Transactions(models.Model):
    date = models.DateField()
    amount = models.IntegerField()
    description = models.CharField(max_length = 200)
    CATEGORY_CHOICES = (
        ('Food', 'Food'),
        ('Personal', 'Personal'),
        ('Health', 'Health'),
        ('Transportation', 'Transportation'),
        ('Clothes', 'Clothes'),
        ('Utilities', 'Utilities'),
        ('Travel', 'Travel'),
        ('Other', 'Other'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
    )
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    PAYMENT_CHOICES = (
        ('PayPay', 'PayPay'),
        ('Cash', 'Cash'),
        ('Credit', 'Credit'),
        ('E-money', 'E-money'),
        ('Bank', 'Bank'),
    )
    payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES)

    
    def __str__(self):
        return self.description
    
    