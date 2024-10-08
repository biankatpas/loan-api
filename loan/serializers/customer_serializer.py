from rest_framework import serializers

from loan.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "name"]
        read_only_fields = ["id", "user"]
