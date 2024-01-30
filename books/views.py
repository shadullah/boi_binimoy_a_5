from django.shortcuts import render
from .models import Books

# Create your views here.
def books(req):
    data = Books.objects.all()
    return render(req, 'books.html', {'data': data})