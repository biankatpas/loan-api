from django.urls import path

from loan.views import (BankListCreateView, BankRetrieveUpdateDestroyAPIView,
                        CustomerListCreateView,
                        CustomerRetrieveUpdateDestroyAPIView)

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
]
