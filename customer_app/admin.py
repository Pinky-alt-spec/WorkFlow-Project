from django.contrib import admin
from .models import Customer
from .models import FinancialRecord


admin.site.register(Customer)

class FinancialRecordAdmin(admin.ModelAdmin):
    list_display = ['customer', 'month', 'income', 'expenses']
    
admin.site.register(FinancialRecord, FinancialRecordAdmin)

