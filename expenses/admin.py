from django.contrib import admin
from .models import Apartment, Expense

# تسجيل نموذج الشقة
@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('number', 'owner_name')  # الحقول التي ستظهر في القائمة
    search_fields = ('number', 'owner_name')  # الحقول القابلة للبحث

# تسجيل نموذج المصروف
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('apartment', 'month', 'amount', 'category', 'color')  # الحقول التي ستظهر في القائمة
    list_filter = ('category', 'month')  # فلاتر للتصفية
    search_fields = ('apartment__number', 'category')  # الحقول القابلة للبحث