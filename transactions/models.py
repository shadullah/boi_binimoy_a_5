from django.db import models
from account.models import UserAccount

# Create your models here.
class Transactions(models.Model):
    account = models.ForeignKey(UserAccount, related_name='transactions', on_delete = models.CASCADE)

    amount = models.DecimalField(max_digits=15, decimal_places = 2)
    balance_after_transaction = models.DecimalField(max_digits=12, decimal_places = 2)
    transaction_type = models.IntegerField(choices = ((1, 'Deposite'),(2, 'Buy'),), null=True)
    timestamp = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['timestamp']