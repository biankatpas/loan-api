from django.urls import path

from loan.views import (BankListCreateView, BankRetrieveUpdateDestroyAPIView,
                        CustomerListCreateView,
                        CustomerRetrieveUpdateDestroyAPIView,
                        LoanListCreateView, LoanRetrieveUpdateDestroyAPIView,
                        PaymentListCreateView,
                        PaymentRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path("banks/", BankListCreateView.as_view(), name="bank-list-create"),
    path(
        "banks/<uuid:pk>/",
        BankRetrieveUpdateDestroyAPIView.as_view(),
        name="bank-detail",
    ),
    path("customers/", CustomerListCreateView.as_view(), name="customer-list-create"),
    path(
        "customers/<uuid:pk>/",
        CustomerRetrieveUpdateDestroyAPIView.as_view(),
        name="customer-detail",
    ),
    path("loans/", LoanListCreateView.as_view(), name="loan-list-create"),
    path(
        "loans/<uuid:pk>/",
        LoanRetrieveUpdateDestroyAPIView.as_view(),
        name="loan-detail",
    ),
    path("payments/", PaymentListCreateView.as_view(), name="payment-list-create"),
    path(
        "payments/<uuid:pk>/",
        PaymentRetrieveUpdateDestroyAPIView.as_view(),
        name="payment-detail",
    ),
]
