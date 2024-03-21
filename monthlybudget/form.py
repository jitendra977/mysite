from datetime import date, datetime ,timezone
from django import forms
from .models import Transactions

class AddTransactionForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['date'].initial = date.today().strftime('%Y-%m-%d')
    class Meta:
        model = Transactions
        fields = ['date', 'amount', 'description', 'category', 'payment_method']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'})
        }
