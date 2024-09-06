from rest_framework import generics

from loan.models import Loan
from loan.serializers import LoanSerializer


class LoanListCreateView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
