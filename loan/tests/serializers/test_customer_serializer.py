import pytest
from rest_framework.exceptions import ValidationError

from loan.serializers import CustomerSerializer
from loan.tests.fixtures.customer_fixtures import create_customer


@pytest.mark.django_db
def test_customer_serializer_valid_data(create_customer):
    customer = create_customer

    serializer = CustomerSerializer(instance=customer)

    assert serializer.data["name"] == customer.name
    assert serializer.data["id"] == str(customer.id)


@pytest.mark.django_db
def test_customer_serializer_invalid_data():
    mock_invalid_data = {
        "name": "",
    }

    serializer = CustomerSerializer(data=mock_invalid_data)

    assert not serializer.is_valid()
    assert "name" in serializer.errors
