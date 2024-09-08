import pytest
from rest_framework import status
from rest_framework.exceptions import ValidationError

from loan.serializers import PaymentSerializer
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
