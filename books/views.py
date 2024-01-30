from django.shortcuts import render
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