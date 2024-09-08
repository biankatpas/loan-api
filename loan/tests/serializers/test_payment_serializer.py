import uuid
from unittest.mock import MagicMock

import pytest
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError

from loan.serializers import LoanDetailSerializer, PaymentSerializer
from loan.tests.fixtures.payment_fixtures import (create_bank, create_customer,
                                                  create_loan, create_payment,
                                                  create_user)


@pytest.mark.django_db
def test_payment_serializer_valid_data(create_payment):
    payment = create_payment

    serializer = PaymentSerializer(instance=payment)

    assert serializer.data["amount"] == str(payment.amount)
    assert serializer.data["payment_date"] == str(payment.payment_date)
    assert serializer.data["loan"]["id"] == str(payment.loan.id)


@pytest.mark.django_db
def test_payment_serializer_representation(create_payment):
    payment = create_payment

    serializer = PaymentSerializer(instance=payment)

    serialized_data = serializer.data

    assert serializer.data["amount"] == str(payment.amount)
    assert serializer.data["payment_date"] == str(payment.payment_date)
    assert serialized_data["loan"] == LoanDetailSerializer(payment.loan).data


@pytest.mark.django_db
def test_payment_serializer_invalid_data(create_payment):
    payment = create_payment

    mock_invalid_data = {
        "amount": "not_a_number",
        "payment_date": payment.payment_date,
        "loan": 1,
    }

    serializer = PaymentSerializer(data=mock_invalid_data)

    assert not serializer.is_valid()
    assert "amount" in serializer.errors


@pytest.mark.django_db
def test_payment_serializer_customer_validation(create_payment):
    payment = create_payment

    invalid_loan_id = str(uuid.uuid4())

    mock_request = MagicMock()
    mock_request.user = payment.loan.customer.user

    serializer = PaymentSerializer(instance=payment, context={"request": mock_request})

    with pytest.raises(serializers.ValidationError) as error_detail:
        serializer.validate_loan(invalid_loan_id)
        assert "Loan does not exist." in str(error_detail.value)


@pytest.mark.django_db
def test_payment_serializer_permission_denied(create_payment):
    payment = create_payment

    mock_request = MagicMock()
    mock_request.user = MagicMock()
    mock_request.user.id = str(uuid.uuid4())

    serializer = PaymentSerializer(instance=payment, context={"request": mock_request})

    with pytest.raises(serializers.ValidationError) as error_detail:
        serializer.validate_loan(payment.loan.id)
        assert "Loan does not belong to the current user." in str(error_detail.value)
