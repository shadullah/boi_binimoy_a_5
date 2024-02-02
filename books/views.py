from django.shortcuts import render,get_object_or_404,redirect
from .models import Books
from . import models
from django.views.generic import DetailView

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

def buyNow(req, book_id):
    book = get_object_or_404(Books, pk=book_id)

    print(book)
    return redirect('home')