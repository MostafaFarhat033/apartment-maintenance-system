from django.shortcuts import render, redirect
from datetime import datetime
from .models import Apartment, Expense
from .forms import ExpenseForm

def yearly_expenses(request, year):  #عرض الجدول السنوي للمصروفات
    apartments = Apartment.objects.all()  # جلب الـ 20 شقة
    months = [datetime(year, month, 1) for month in range(1, 13)]  # الأشهر الـ 12
    expenses = Expense.objects.filter(month__year=year)  # المصروفات للسنة
    
    expense_data = {}
    for apartment in apartments:
        expense_data[apartment] = {}
        for month in months:
            expense_on_month = expenses.filter(apartment=apartment, month=month).first()
            expense_data[apartment][month.strftime('%Y-%m')] = expense_on_month
    
    context = {
        'year': year,
        'expense_data': expense_data,
        'months': [month.strftime('%Y-%m') for month in months],
    }
    return render(request, 'yearly_expenses.html', context)


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_url')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})