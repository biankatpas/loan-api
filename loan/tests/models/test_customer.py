import uuid
import pytest

from loan.models import Customer
from loan.tests.fixtures.customer_fixtures import create_customer


@pytest.mark.django_db
def test_customer_creation(create_customer):
    customer = create_customer

    expected_result = {
        "name": "Customer Name",
    }

    assert isinstance(customer, Customer)
    assert isinstance(customer.id, uuid.UUID)
    assert customer.name == expected_result["name"]


@pytest.mark.django_db
def test_customer_str(create_customer):
    customer = create_customer
    assert str(customer) == "Customer Name"
