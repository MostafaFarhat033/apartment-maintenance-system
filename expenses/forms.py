from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['apartment', 'month', 'amount', 'category', 'color']  # Use 'apartments' instead of 'apartment'
        labels = {
            'apartment': 'الشقق',  # Update label to match the field name
            'month': 'الشهر',
            'amount': 'المبلغ',
            'category': 'الفئة',
            'color': 'اللون',
        }
        widgets = {
            'month': forms.DateInput(attrs={'type': 'month'}),  # اختيار الشهر فقط
        }