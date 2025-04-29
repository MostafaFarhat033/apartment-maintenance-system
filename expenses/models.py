from django.db import models

class Apartment(models.Model):
    apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE)  # الشقق المرتبطة
    number = models.IntegerField(unique=True)  # رقم الشقة (من 1 إلى 20)
    owner_name = models.CharField(max_length=100)  # اسم المالك (اختياري)
    phone_number = models.CharField(max_length=20, blank=True)  # رقم الهاتف (اختياري)
    
    def get_apartments_display(self):
        return ", ".join([str(apartment) for apartment in self.apartments.all()])
    get_apartments_display.short_description = "الشقق المرتبطة"

    
    
class Expense(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)  # Likely the correct field
    month = models.DateField()  # الشهر (مثل 2023-10-01 لشهر أكتوبر)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # المبلغ
    category = models.CharField(max_length=50, choices=[
        ('motor', 'الماتور'),
        ('electricity', 'الكهرباء'),
        ('water_bill', 'فاتورة المياه'),
        ('elevator_maintenance', 'صيانة الاسانسير'),
        ('other', 'أخرى'),
    ])  # فئة المصروف
    color = models.CharField(max_length=20)  # اللون للعرض في الجدول

    def __str__(self):
        apartments_list = ", ".join([str(apartment) for apartment in self.apartments.all()])
        return f"{apartments_list} - {self.month.strftime('%Y-%m')} - {self.category}"

    def clean(self):
        from django.core.exceptions import ValidationError
        # منع تكرار المصروف لنفس الشقة في نفس الشهر لنفس الفئة
        for apartment in self.apartments.all():
            if Expense.objects.filter(
                apartments__id=apartment.id,  # Use apartments__id to filter by the related apartment
                month=self.month,
                category=self.category
            ).exclude(id=self.id).exists():
                raise ValidationError(f"يوجد بالفعل مصروف لهذه الشقة ({apartment}) في هذا الشهر لهذه الفئة.")