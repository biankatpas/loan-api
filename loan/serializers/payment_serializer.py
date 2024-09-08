from rest_framework import serializers

from loan.models import Customer, Loan, Payment
from loan.serializers import LoanDetailSerializer


class PaymentSerializer(serializers.ModelSerializer):
    loan = serializers.UUIDField()

    class Meta:
        model = Payment
        fields = "__all__"

    def validate_loan(self, value):
        try:
            loan = Loan.objects.get(id=value)
        except Loan.DoesNotExist:
            raise serializers.ValidationError("Loan does not exist.")

        request_user = self.context["request"].user
        if loan.customer.user != request_user:
            raise serializers.ValidationError(
                "You do not have permission to access this loan payment because customer does not belong to the current user."
            )

        return loan

    def create(self, validated_data):
        return Payment.objects.create(**validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["loan"] = LoanDetailSerializer(instance.loan).data
        return representation
