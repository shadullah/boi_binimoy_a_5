from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from books.models import Books
from categories.models import Category
# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    Model = Books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books']=Books.objects.all()
        # print(context)
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = Category.objects.get(slug = category_slug )
            context['books'] = Books.objects.filter(category=category)
        context['category']=Category.objects.all()
        return context
    