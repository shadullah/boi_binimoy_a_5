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
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
RATING_NO=(
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

class Comment(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='name')
    rating = models.IntegerField(choices=RATING_NO)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.name)