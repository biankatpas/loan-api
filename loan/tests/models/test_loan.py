import uuid
import pytest

from loan.models import Loan
from loan.tests.fixtures.loan_fixtures import create_loan, create_bank, create_customer


@pytest.mark.django_db
def test_loan_creation(create_loan):
    expected_bank = {
        "name": "Banco do Brasil", "code": "001"
    }
    expected_customer = {
        "name": "Customer Name",
    }
    expected_loan = {
        "nominal_value": 10000.00,
        "interest_rate": 5.00,
        "request_ip_address": "192.168.1.1"
    }

    loan = create_loan

    assert isinstance(loan, Loan)
    assert isinstance(loan.id, uuid.UUID)
    assert loan.nominal_value == expected_loan["nominal_value"]
    assert loan.interest_rate == expected_loan["interest_rate"]
    assert loan.request_ip_address == expected_loan["request_ip_address"]
    assert loan.bank.name == expected_bank["name"]
    assert loan.bank.code == expected_bank["code"]
    assert loan.customer.name == expected_customer["name"]


@pytest.mark.django_db
def test_loan_str(create_loan):
    loan = create_loan

    assert str(loan) == f"Loan {loan.id} - Value: {loan.nominal_value}, Interest Rate: {loan.interest_rate}"
