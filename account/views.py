from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import UserRegForm
from django.contrib.auth import login

# Create your views here.
class UserRegistration(FormView):
    template_name='account/user_reg.html'
    form_class = UserRegForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(user)
        return super().form_valid(form)