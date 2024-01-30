from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import FormView,UpdateView
from .forms import UserRegForm, UserUpdateForm
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView
from . import forms
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

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

# class UserProfileUpdateView(View):
#     template_name = 'account/profile.html'
    # model = UserAccount
    # success_url = reverse_lazy('profile')
    # form_class = UpdateUserForm
    # pk_url_kwarg = 'id'
    
    # def get(self, request):
    #     form = UpdateUserForm(instance=request.user)
    #     return render(request, self.template_name, {'form':form})
    
    # def post(self, request):
    #     form = UpdateUserForm(request.POST, instance=request.user)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('profile')
    #     return render(request, self.template_name, {'form': form})

#     template_name = 'account/profile.html'

#     def get(self, request):
#         form = UpdateUserForm(instance=request.user)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = UpdateUserForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')  # Redirect to the user's profile page
#         return render(request, self.template_name, {'form': form})

def editProfile(req):
    if req.method == 'POST':
        print(req)
        edit_form = forms.UserUpdateForm(req.POST, instance=req.user)
        if edit_form.is_valid():
            print('hi aldfls')
            edit_form.save()
            return redirect('profile')
        else:
            print("invalid form")
    else:
        edit_form = forms.UserRegForm(instance=req.user)
    return render(req, 'account/profile.html', {'form' : edit_form})

# class UserProfileUpdateView(LoginRequiredMixin,UpdateView):
#     template_name = 'account/profile.html'
#     form_class = UserUpdateForm
#     success_url = reverse_lazy('profile')
#     def get_object(self):
#         return self.request.user
    
#     def form_valid(self, form):
#         # messages.success(self.request, 'Profile Updated Successfully')
#         return super().form_valid(form)
    
#     def form_invalid(self, form):
#         # messages.danger(self.request, 'Information Incorrect')
#         return super().form_invalid(form)