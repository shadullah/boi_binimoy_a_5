from django.contrib import admin
from .models import Transactions
# Register your models here.
@admin.register(Transactions)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'balance_after_transaction']