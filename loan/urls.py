from django.urls import path

from loan.views import BankDetailView, BankListCreateView

urlpatterns = [
    path("banks/", BankListCreateView.as_view(), name="bank-list-create"),
    path("banks/<uuid:pk>/", BankDetailView.as_view(), name="bank-detail"),
]
