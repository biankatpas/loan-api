import pytest
from django.utils import timezone

from loan.models import Payment
from loan.tests.fixtures.bank_fixtures import create_bank
from loan.tests.fixtures.customer_fixtures import create_customer
from loan.tests.fixtures.loan_fixtures import create_loan


@pytest.fixture
def create_payment(create_bank, create_customer, create_loan):
    return Payment.objects.create(
        loan=create_loan, payment_date=timezone.now().date(), amount=500.00
    )
