from rest_framework import serializers

from loan.models import Bank, Customer, Loan
from loan.serializers import BankSerializer, CustomerSerializer


class LoanCreateSerializer(serializers.ModelSerializer):
    customer = customer = serializers.UUIDField()
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.all())

    class Meta:
        model = Loan
        fields = "__all__"

    def create(self, validated_data):
        customer_uuid = validated_data.pop("customer")
        try:
            customer = Customer.objects.get(id=customer_uuid)
        except Customer.DoesNotExist:
            raise serializers.ValidationError("Customer does not exist.")

        if customer.user != self.context["request"].user:
            raise serializers.ValidationError(
                "Customer does not belong to the current user."
            )

        loan = Loan.objects.create(customer=customer, **validated_data)
        return loan

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
        customer_uuid = value
        request_user = self.context["request"].user

        try:
            customer = Customer.objects.get(id=customer_uuid)
        except Customer.DoesNotExist:
            raise serializers.ValidationError("Customer does not exist.")
        if customer.user != request_user:
            raise serializers.ValidationError(
                "Customer does not belong to the current user."
            )
        return customer
