from django.urls import path 
from . import views 

urlpatterns = [
    path('All_books', views.booksAll, name='books'),
    path('details/<int:id>', views.DetailBook.as_view(), name='details'),
    path("buy/<int:book_id>", views.buyNow, name='buy'),
]
