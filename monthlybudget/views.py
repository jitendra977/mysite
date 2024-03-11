from django.shortcuts import redirect, render
from monthlybudget.form import  AddTransactionForm

from monthlybudget.models import Transactions

# Create your views here.
def budget_home(request):
    trans = Transactions.objects.all()
    return render(request, 'budget_home.html',{'transactions':trans})

def add_transactions(request):
    if request.method == 'POST':
        form = AddTransactionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/budget_home/')
    else:  # This else should be aligned with the outer if block
        form = AddTransactionForm()
    return render(request, 'add_transactions.html', {'form': form})
