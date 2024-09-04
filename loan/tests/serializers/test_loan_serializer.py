import pytest

from rest_framework.exceptions import ValidationError
from rest_framework import status

from loan.serializers import LoanSerializer
from loan.tests.fixtures.loan_fixtures import create_loan, create_bank, create_customer


@pytest.mark.django_db
def test_loan_serializer_valid_data(create_loan):
    loan = create_loan

    mock_valid_data = {
        'nominal_value': loan.nominal_value,
        'interest_rate': loan.interest_rate,
        'request_date': loan.request_date,
        'request_ip_address': loan.request_ip_address,
        'bank': loan.bank.id,
        'customer': loan.customer.id
    }

    serializer = LoanSerializer(data=mock_valid_data)

    assert serializer.is_valid()
    assert serializer.validated_data['nominal_value'] == loan.nominal_value
    assert serializer.validated_data['interest_rate'] == loan.interest_rate
    assert serializer.validated_data['request_ip_address'] == loan.request_ip_address
    assert serializer.validated_data['bank'] == loan.bank
    assert serializer.validated_data['customer'] == loan.customer


@pytest.mark.django_db
def test_loan_serializer_invalid_data(create_loan):
    loan = create_loan

    mock_invalid_data = {
        'nominal_value': 'not_a_number',
        'interest_rate': loan.interest_rate,
        'request_date': loan.request_date,
        'request_ip_address': loan.request_ip_address,
        'bank': 1,
        'customer': 1
    }

    serializer = LoanSerializer(data=mock_invalid_data)

    assert not serializer.is_valid()
    assert 'nominal_value' in serializer.errors
