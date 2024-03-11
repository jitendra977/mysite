from django import forms

from monthlybudget.models import Transactions


class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = '__all__'