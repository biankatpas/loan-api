from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from loan.models import Payment
from loan.permissions import IsPaymentOwner
from loan.serializers import PaymentSerializer


class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Payment.objects.filter(loan__customer__user=user)


class PaymentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsPaymentOwner]

    def get_queryset(self):
        user = self.request.user
        return Payment.objects.filter(loan__customer__user=user)
