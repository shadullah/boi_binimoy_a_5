from django.db import models
from django.contrib.auth.models import User
from books.models import Books
from account.models import UserAccount
from transactions.models import Transactions
# Create your models here.
class BorrowBook(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Books, on_delete = models.CASCADE, default=1)
    user_acc = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True, default=1, blank=True)
    borrow_date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.book}"