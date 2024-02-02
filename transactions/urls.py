from django.urls import path
from .views import depositeview,TransactionReportView
from . import views

urlpatterns = [
    path("deposite/", depositeview.as_view(), name='deposite'),
    path("report/", TransactionReportView.as_view(), name='report'),
]
