from django.contrib import admin

from .models import Bank, Customer, Loan, Payment


admin.site.register(Bank)
admin.site.register(Customer)
admin.site.register(Loan)
admin.site.register(Payment)
