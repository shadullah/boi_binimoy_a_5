from typing import Any
from django.shortcuts import render,get_object_or_404,redirect
from .models import Books
from . import models
from django.views.generic import DetailView
from account.models import UserAccount
from django.contrib import messages
from borrow_books.models import BorrowBook
# from django.contrib.auth.decorators import @login
from django.contrib.auth.decorators import login_required
from . import forms 
from django.views import View
from borrow_books.models import BorrowBook

# Create your views here.
def books(req):
    data = Books.objects.all()
    return render(req, 'books.html', {'data': data})

class DetailBook(DetailView):
    model = models.Books
    pk_url_kwarg = 'id'
    template_name = 'books.html'

    def post(self, req, *args, **kwargs):
        cmmnt_form = forms.CommentForm(data=self.request.POST)
        book = self.get_object()
        if cmmnt_form.is_valid():
            new_com = cmmnt_form.save(commit=False)
            new_com.book = book
            new_com.save()
            print(new_com)
        return self.get(req, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        book = self.object
        comments = book.comments.all()
        cmmnt_form = forms.CommentForm()
        # print(cmmnt_form)
        if self.request.user:
            borrow = BorrowBook.objects.filter(book=book).first()

        if borrow:
            cmmnt_form = forms.CommentForm()
        else:
            cmmnt_form = None

        context['comments'] = comments
        context['com_form']= cmmnt_form
        return context
    # model = models.Books
    # pk_url_kwarg = 'id'
    # template_name = 'books.html'

    # def post(self, req, *args, **kwargs):
    #     com_form = forms.CommentForm(data=self.request.POST)
    #     book = self.get_object()
    #     # print(com_form)
    #     if com_form.is_valid():
    #         new_com = com_form.save(commit=False)
    #         new_com.book = book
    #         # print(new_com)
    #         new_com.save()
    #     print(req)
    #     return self.get(req, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     book = self.object 
    #     comments = book.comments.all()
    #     com_form = forms.CommentForm()
    #     # borrow = BorrowBook.objects.get(user = self.request.user)
    #     borrow = BorrowBook.objects.filter(user=self.request.user, book=book).first()

    #     if borrow:
    #         com_form = forms.CommentForm()
    #     else:
    #         com_form = None

    #     # print(com_form)
    #     context['comments'] = comments
    #     context['com_form'] = com_form
    #     return context

def booksAll(req):
    data = Books.objects.all()
    return render(req, 'booksAll.html', {'books': data})

def borrow(req):
    borrow , created = BorrowBook.objects.get_or_create(user=req.user)
    books = borrow.books.all()
    print(books)
    return render(req, 'accounts/profile.html',{'books': books})

@login_required
def buyNow(req, book_id):
    book = Books.objects.filter(id=book_id).first()

    # book = get_object_or_404(Books, pk=book_id)
    # user_tag = UserAccount.objects.all(user=req.user)
    user_acc = get_object_or_404(UserAccount,user=req.user)
    acc_balance = user_acc.balance
    bookPrice = book.price

    if acc_balance >=bookPrice:
        acc_balance -= bookPrice
        user_acc.balance = acc_balance
        # user_acc.balance -= bookPrice
        # messages.success(req,"Check your transaction")
        user_acc.save()

        profile, created = BorrowBook.objects.get_or_create(user=req.user, book = book)
        print(profile)
        # profile.borrow_books.add(book)
    else:
        print("not eror")
        messages.error(req,"Your Balance is not sufficient.")
        redirect("deposite")

    return redirect('profile')


def pay(req, id):
    user_acc = get_object_or_404(UserAccount, user=req.user)
    print(user_acc.balance)
    book = get_object_or_404(BorrowBook, id=id)

    if book.returned:
        messages.error(req, "You have already paid for this")
        print("error")
    else:
        print("success")
        book_price = book.book.price
        user_acc.balance += book_price
        user_acc.save(update_fields=["balance"])
        book.returned = True
        book.save(update_fields=["returned"])
        messages.success(req, " payment successful")
    return redirect('profile')