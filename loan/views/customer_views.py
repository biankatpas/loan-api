from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from loan.models import Customer
from loan.permissions import IsCustomerOwner
from loan.serializers import CustomerSerializer


class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, IsCustomerOwner]

    def get_queryset(self):
        user = self.request.user
        return Customer.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    permission_classes = [IsAuthenticated, IsCustomerOwner]

    def get_queryset(self):
        user = self.request.user
        return Customer.objects.filter(user=user)
