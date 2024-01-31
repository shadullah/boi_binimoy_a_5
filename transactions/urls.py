from django.urls import path
from .views import depositeview,TransactionReportView

urlpatterns = [
    path("deposite/", depositeview.as_view(), name='deposite'),
    path("report/", TransactionReportView.as_view(), name='report')
]
