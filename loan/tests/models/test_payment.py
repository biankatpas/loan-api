import uuid
import pytest

from loan.models import Payment
from loan.tests.fixtures.payment_fixtures import create_loan, create_bank, create_customer, create_payment


@pytest.mark.django_db
def test_payment_creation(create_payment):
    expected_payment = {
        "amount": 500.00,
    }

    payment = create_payment

    assert isinstance(payment, Payment)
    assert isinstance(payment.id, uuid.UUID)
    assert payment.amount == expected_payment["amount"]


@pytest.mark.django_db
def test_payment_str(create_payment):
    payment = create_payment

    assert str(payment) == f"Payment {payment.id} - Loan: {payment.loan.id} - Amount: {payment.amount}"
