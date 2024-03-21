from datetime import date, datetime, timezone
from django.shortcuts import redirect, render
from django.db.models import Sum
from monthlybudget.form import AddTransactionForm
from monthlybudget.models import Transactions

from django.db.models import Sum
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Transactions  # Assuming you have a Transactions model defined in models.py
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Sum,Q

def budget_home(request):
    # Get today's date
    today = date.today()

    # Set default values for fromdate and todate
    fromdate_str = request.GET.get('fromdate', date(today.year, today.month, 1).strftime("%Y-%m-%d"))
    todate_str = request.GET.get('todate', date(today.year, today.month, today.day).strftime("%Y-%m-%d"))
    selected_category  = request.GET.get('category')
    # Convert the date strings to datetime objects
    fromdate = datetime.strptime(fromdate_str, '%Y-%m-%d').date()
    todate = datetime.strptime(todate_str, '%Y-%m-%d').date()
    

    # Construct the queryset with date range filter
    transactions = Transactions.objects.filter(
        date__range=[fromdate, todate]
    ).order_by('-date')

    # Apply additional filter condition if a category is selected
    if selected_category and selected_category != '':  # Check if category is selected and not 'All'
        transactions = transactions.filter(category=selected_category)
       

    # Calculate the total amount of all transactions
    total_amount = transactions.aggregate(total_amount=Sum('amount'))['total_amount'] or 0

    # Calculate the total amount for each category of transactions
    category_totals = transactions.values('category').annotate(total=Sum('amount'))

    #category name 
    transactions_category = Transactions.objects.values_list('category',flat=True).distinct()
    
    # Construct a context dictionary
    context = {'transactions': transactions, 'total_amount': total_amount,'category':transactions_category}

    # Add category totals to the context dynamically
    for category_total in category_totals:
        # If the total amount for a category is None or zero, set it to zero
        total = category_total['total'] if category_total['total'] is not None and category_total['total'] > 0 else 0
        context[category_total['category'].lower()] = total 
    
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
