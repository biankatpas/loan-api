import pytest
from django.utils import timezone
from faker import Faker

from loan.models import Payment
from loan.tests.fixtures.bank_fixtures import create_bank
from loan.tests.fixtures.customer_fixtures import create_customer
from loan.tests.fixtures.loan_fixtures import create_loan

fake = Faker()


@pytest.fixture
def create_payment(create_bank, create_customer, create_loan):
    fake_payment_date = fake.date_this_year()
    fake_amount = round(fake.pydecimal(left_digits=3, right_digits=2, positive=True), 2)

    return Payment.objects.create(
        loan=create_loan, payment_date=fake_payment_date, amount=fake_amount
    )
