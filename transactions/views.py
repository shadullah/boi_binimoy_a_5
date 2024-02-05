from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from .models import Transactions
from django.contrib import messages
from .forms import DepositeForm, BuyForm
from datetime import datetime
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from books.models import Books
from account.models import UserAccount
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string

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
        mail_subject = "Deposite Message"
        message = render_to_string('transactions/deposite_mail.html', {
            'user': self.request.user,
            'amount': amount,
        })
        to_email = self.request.user.email 
        send_email = EmailMultiAlternatives(mail_subject, message, to=[to_email])
        send_email.attach_alternative(message, "text/html")
        # send_email.send()
        messages.success(self.request, f"{amount}$ was deposited to your account successfully!!")
        return super().form_valid(form)
    
# @login_required
# class Buyview(TransactionCreateMixin):
#     form_class = BuyForm
    
#     def get_initial(self):
#         initial = {'transaction_type': 2}
#         return initial
    
#     def form_valid(self, form):
#         amount = form.cleaned_data.get('amount')
#         account = self.request.user.account
#         account.balance -= amount
#         account.save(
#             update_fields = ['balance']
#         )
#         messages.success(self.request, f"{amount}$ was cut off from your account")
#         return super().form_valid(form)
    

# def buy(request, id):
#     book = Books.objects.filter(id=id).first()
#     user_account = get_object_or_404(UserAccount, user=request.user)
#     user_tk = user_account.balance

#     if user_tk >= book.price:
#         user_tk -= book.price
#         user_account.save(update_fields=["balance"])


#     print(user_tk)
#     return redirect('home')

    
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