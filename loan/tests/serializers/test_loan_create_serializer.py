import uuid
from unittest.mock import MagicMock

import pytest
from faker import Faker

from loan.serializers import (BankSerializer, CustomerSerializer,
                              LoanCreateSerializer)
from loan.tests.fixtures.loan_fixtures import (create_bank, create_customer,
                                               create_loan, create_user)

fake = Faker()


@pytest.mark.django_db
def test_loan_create_serializer_valid_data(
    create_customer,
    create_bank,
):
    customer = create_customer
    bank = create_bank

    fake_nominal_value = round(
        fake.pydecimal(left_digits=5, right_digits=2, positive=True), 2
    )
    fake_interest_rate = round(
        fake.pydecimal(left_digits=1, right_digits=2, positive=True), 2
    )
    fake_request_date = fake.date_this_decade()
    fake_request_ip_address = fake.ipv4()

    data = {
        "customer": str(customer.id),
        "bank": bank.id,
        "nominal_value": fake_nominal_value,
        "interest_rate": fake_interest_rate,
        "request_date": fake_request_date,
    }

    mock_request = MagicMock()
    mock_request.user = customer.user

    serializer = LoanCreateSerializer(data=data, context={"request": mock_request})

    assert serializer.is_valid()
    loan = serializer.save()

    assert loan.customer == customer
    assert loan.bank == bank
    assert loan.nominal_value == fake_nominal_value
    assert loan.interest_rate == fake_interest_rate
    assert loan.request_date == fake_request_date


@pytest.mark.django_db
def test_loan_create_serializer_representation(create_loan):
    loan = create_loan

    serializer = LoanCreateSerializer(instance=loan)

    serialized_data = serializer.data

    assert serialized_data["customer"] == CustomerSerializer(loan.customer).data
    assert serialized_data["bank"] == BankSerializer(loan.bank).data
    assert serialized_data["nominal_value"] == str(loan.nominal_value)
    assert serialized_data["interest_rate"] == str(loan.interest_rate)
    assert serialized_data["request_date"] == str(loan.request_date)


@pytest.mark.django_db
def test_loan_create_serializer_customer_validation(create_bank):
    bank = create_bank

    serializer = LoanCreateSerializer(
        data={
            "customer": str(uuid.uuid4()),
            "bank": bank.id,
            "nominal_value": "1.00",
            "interest_rate": "1.00",
            "request_date": "2024-01-01",
            "request_ip_address": fake.ipv4(),
        }
    )

    assert not serializer.is_valid()
    assert "customer" in serializer.errors
    assert "Customer does not exist." in serializer.errors["customer"]


@pytest.mark.django_db
def test_loan_create_serializer_permission_denied(
    create_customer, create_bank, create_user
):
    customer = create_customer
    bank = create_bank
    other_user = create_user

    data = {
        "customer": str(customer.id),
        "bank": bank.id,
        "nominal_value": "10000.00",
        "interest_rate": "5.00",
        "request_date": "2024-01-01",
        "request_ip_address": fake.ipv4(),
    }

    mock_request = MagicMock()
    mock_request.user = other_user

    serializer = LoanCreateSerializer(data=data, context={"request": mock_request})

    assert not serializer.is_valid()
    assert "customer" in serializer.errors
    assert (
        "You do not have permission to access this loan because customer does not belong to the current user."
        in serializer.errors["customer"]
    )
