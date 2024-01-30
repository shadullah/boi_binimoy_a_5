from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from books.models import Books
# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    Model = Books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books']=Books.objects.all()
        # print(context)
        # context['category']=b
        return context
    