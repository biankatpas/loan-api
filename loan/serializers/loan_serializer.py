from rest_framework import serializers

from loan.models import Bank, Customer, Loan
from loan.serializers import BankSerializer, CustomerSerializer


class LoanCreateSerializer(serializers.ModelSerializer):
    customer = customer = serializers.UUIDField()
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())

    class Meta:
        model = Loan
        fields = "__all__"

    def validate_customer(self, value):
        try:
            customer = Customer.objects.get(id=value)
        except Customer.DoesNotExist:
            raise serializers.ValidationError("Customer does not exist.")

        request_user = self.context["request"].user
        if customer.user != request_user:
            raise serializers.ValidationError(
                "You do not have permission to access this loan because customer does not belong to the current user."
            )
        return customer

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["customer"] = CustomerSerializer(instance.customer).data
        representation["bank"] = BankSerializer(instance.bank).data
        return representation


class LoanDetailSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    bank = BankSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = "__all__"

    def validate_customer(self, value):
        try:
            customer = Customer.objects.get(id=value)
        except Customer.DoesNotExist:
            raise serializers.ValidationError("Customer does not exist.")

        request_user = self.context["request"].user
        if customer.user != request_user:
            raise serializers.ValidationError(
                "You do not have permission to access this loan because customer does not belong to the current user."
            )
        return customer
