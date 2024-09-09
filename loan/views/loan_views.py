from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from loan.models import Loan
from loan.permissions import IsLoanOwner
from loan.serializers import LoanCreateSerializer, LoanDetailSerializer


class LoanListCreateView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return LoanCreateSerializer
        return LoanDetailSerializer

    def get_queryset(self):
        user = self.request.user
        return Loan.objects.filter(customer__user=user)

    def perform_create(self, serializer):
        remote_addr = self.request.META.get("REMOTE_ADDR")
        serializer.save(request_ip_address=remote_addr)


class LoanRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    permission_classes = [IsAuthenticated, IsLoanOwner]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return LoanCreateSerializer
        return LoanDetailSerializer

    def get_queryset(self):
        user = self.request.user
        return Loan.objects.filter(customer__user=user)
