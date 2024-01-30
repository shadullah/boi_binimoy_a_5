from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import UserRegForm
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView

# Create your views here.
class UserRegistration(FormView):
    template_name='account/user_reg.html'
    form_class = UserRegForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name='account/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
def user_logout(req):
    logout(req)
    return redirect('login')