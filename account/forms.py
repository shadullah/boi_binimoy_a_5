from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegForm(UserCreationForm):
    class Meta:
        model= User 
        fields = ['username', 'password1','password2', 'first_name', 'last_name', 'email']
    def save(self, commit=False):
        our_user = super().save(commit=False)
        if commit== True:
            our_user.save()
        return our_user