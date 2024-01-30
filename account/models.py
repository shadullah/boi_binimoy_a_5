from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.account_no)