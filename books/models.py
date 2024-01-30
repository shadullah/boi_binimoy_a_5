from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to='books/static/img/', blank=True, null=True)
    category = models.ManyToManyField(Category)
    

    def __str__(self):
        return self.title