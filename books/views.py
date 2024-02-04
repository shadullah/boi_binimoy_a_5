from django.shortcuts import render,get_object_or_404,redirect
from .models import Books
from . import models
from django.views.generic import DetailView
from account.models import UserAccount
from django.contrib import messages
from borrow_books.models import BorrowBook
# from django.contrib.auth.decorators import @login
from django.contrib.auth.decorators import login_required

# Create your views here.
def books(req):
    data = Books.objects.all()
    return render(req, 'books.html', {'data': data})

class DetailBook(DetailView):
    model = models.Books
    pk_url_kwarg = 'id'
    template_name = 'books.html'

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