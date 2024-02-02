from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places = 2)

    def __str__(self):
        return str(self.account_no)
    
class profile(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.user
