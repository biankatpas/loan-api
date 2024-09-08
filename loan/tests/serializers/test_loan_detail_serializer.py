import uuid
from unittest.mock import MagicMock

import pytest
from faker import Faker
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from loan.serializers import LoanDetailSerializer
from loan.tests.fixtures.loan_fixtures import (create_bank, create_customer,
                                               create_loan, create_user)

fake = Faker()


@pytest.mark.django_db
def test_loan_detail_serializer_valid_data(create_loan):
    loan = create_loan

    mock_request = MagicMock()
    mock_request.user = loan.customer.user

    serializer = LoanDetailSerializer(instance=loan, context={"request": mock_request})

    serialized_data = serializer.data

    assert serialized_data["customer"]["id"] == str(loan.customer.id)
    assert serialized_data["bank"]["id"] == str(loan.bank.id)
    assert serialized_data["nominal_value"] == str(loan.nominal_value)
    assert serialized_data["interest_rate"] == str(loan.interest_rate)
    assert serialized_data["request_date"] == str(loan.request_date)
    assert serialized_data["request_ip_address"] == loan.request_ip_address


@pytest.mark.django_db
def test_loan_detail_serializer_customer_validation(create_loan):
    loan = create_loan

    invalid_customer_id = str(uuid.uuid4())

    mock_request = MagicMock()
    mock_request.user = loan.customer.user

    serializer = LoanDetailSerializer(instance=loan, context={"request": mock_request})

    with pytest.raises(serializers.ValidationError) as error_detail:
        serializer.validate_customer(invalid_customer_id)
        assert "Customer does not exist." in str(error_detail.value)


@pytest.mark.django_db
def test_loan_detail_serializer_permission_denied(
    create_bank, create_customer, create_loan
):
    loan = create_loan

    mock_request = MagicMock()
    mock_request.user = MagicMock()
    mock_request.user.id = str(uuid.uuid4())

    serializer = LoanDetailSerializer(instance=loan, context={"request": mock_request})

    with pytest.raises(serializers.ValidationError) as error_detail:
        serializer.validate_customer(loan.customer.id)
        assert "Customer does not belong to the current user." in str(
            error_detail.value
        )
