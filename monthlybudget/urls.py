

from django.urls import path

from monthlybudget.views import add_transactions, budget_home


urlpatterns = [
    path('',budget_home,name = 'budget_home'),
    path('budget_home/',budget_home,name = 'budget_home'),
    path('add_transactions/',add_transactions,name='add_transactions'),
]
