from django import forms
from .models import Transactions

class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['date', 'amount', 'description', 'category', 'payment_method']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}, choices=[('', 'Select category')] + list(Transactions.CATEGORY_CHOICES)),
            'payment_method': forms.Select(attrs={'class': 'form-select'}, choices=[('', 'Select payment method')] + list(Transactions.PAYMENT_CHOICES))
        }
