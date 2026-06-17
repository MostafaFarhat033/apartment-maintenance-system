from django.urls import path
from .views import yearly_expenses, add_expense, home
from django.shortcuts import redirect
from datetime import datetime



urlpatterns = [
    path('', home, name='home'),
    path('expenses/<int:year>/', yearly_expenses, name='yearly_expenses'),
    path('add-expense/', add_expense, name='add_expense'),
]