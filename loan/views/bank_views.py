from rest_framework import generics

from loan.models import Bank
from loan.serializers import BankSerializer


class BankListCreateView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
