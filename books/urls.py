from django.urls import path 
from . import views 

urlpatterns = [
    path('details/<int:id>', views.DetailBook.as_view(), name='details')
]
