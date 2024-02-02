from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Transactions

class TransactionForm(forms.ModelForm):    
    class Meta:
        model = Transactions
        fields = ["amount", "transaction_type"]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args,**kwargs)
        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput()

    def save(self,commit = True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save(commit)
    
class DepositeForm(TransactionForm):
    def clean_amount(self):
        min_depo_amount = 10
        amount = self.cleaned_data.get('amount')
        if amount < min_depo_amount:
            raise forms.ValidationError(
                f'you need at least {min_depo_amount} to deposite'
            )
        return amount
    
class BuyForm(TransactionForm):
    def clean_amount(self):
        account = self.account
        balance = account.balance
        amount = self.cleaned_data.get["amount"]
        if balance < amount:
            raise forms.ValidationError(
                f'You do not have enough balance in your account. Your balance: {balance}'
            )
        return amount
    