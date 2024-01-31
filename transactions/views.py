from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from .models import Transactions
from django.contrib import messages
from .forms import DepositeForm
from datetime import datetime
from django.db.models import Sum

# Create your views here.
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transactions/transaction_form.html'
    model = Transactions
    title = ''
    success_url = reverse_lazy('report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account 
        })

        return kwargs

    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs) 
        context.update({
            'title': self.title  
        })
        return context
    
class depositeview(TransactionCreateMixin):
    form_class = DepositeForm
    title = "Deposite"

    def get_initial(self):
        initial = {'transaction_type': 1}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(
            update_fields = ['balance']
        )
        messages.success(self.request, f"{amount}$ was deposited to your account successfully!!")
        return super().form_valid(form)
    
class TransactionReportView(LoginRequiredMixin, ListView):
    template_name = 'transactions/report.html'
    model = Transactions
    balance=0

    def get_queryset(self):
        # jodi user kono filter na kore taile full data show krbe
        queryset = super().get_queryset().filter(
            account = self.request.user.account 
        )
        
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date() 
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

            queryset = queryset.filter(timestamp__date__gte = start_date, timestamp__date__lte = end_date)

            self.balance = Transactions.objects.filter(timestamp__date__gte = start_date, timestamp__date__lte = end_date).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance

        return queryset.distinct()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account 
        })
        return context