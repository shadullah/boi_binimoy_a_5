from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import UserAccount

class UserRegForm(UserCreationForm):
    class Meta:
        model= User 
        fields = ['username', 'password1','password2', 'first_name', 'last_name', 'email']

    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()

            UserAccount.objects.create(
                user = our_user,
                account_no = 10000+ our_user.id 
            )
        return our_user
        
class UserUpdateForm(forms.ModelForm):
    # password = None
    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'email']
