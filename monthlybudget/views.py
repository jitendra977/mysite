from django.shortcuts import redirect, render
from django.db.models import Sum
from monthlybudget.form import AddTransactionForm
from monthlybudget.models import Transactions

def budget_home(request):
    # Retrieve all transactions from the database
    transactions = Transactions.objects.all()
    
    # Calculate the total amount of all transactions
    total_amount = transactions.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    
    # Calculate the total amount for each category of transactions
    category_totals = transactions.values('category').annotate(total=Sum('amount'))
    
    # Construct a context dictionary
    context = {'transactions': transactions, 'total_amount': total_amount}
    
    # Add category totals to the context dynamically
    for category_total in category_totals:
        context[category_total['category'].lower()] = category_total['total']
    return render(request, 'budget_home.html', context)


def add_transactions(request):
    if request.method == 'POST':
        form = AddTransactionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('budget_home')
    else:
        form = AddTransactionForm()
    return render(request, 'add_transactions.html', {'form': form})
