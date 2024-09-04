import pytest

from django.utils import timezone

from loan.models import Loan
from loan.tests.fixtures.bank_fixtures import create_bank
from loan.tests.fixtures.customer_fixtures import create_customer


@pytest.fixture
def create_loan(create_bank, create_customer):
    return Loan.objects.create(
        nominal_value=10000.00,
        interest_rate=5.00,
        request_date=timezone.now().date(),
        request_ip_address="192.168.1.1",
        bank=create_bank,
        customer=create_customer
    )
