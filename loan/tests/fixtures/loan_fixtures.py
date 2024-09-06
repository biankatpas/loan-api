import pytest
from faker import Faker

from loan.models import Loan
from loan.tests.fixtures.bank_fixtures import create_bank
from loan.tests.fixtures.customer_fixtures import create_customer

fake = Faker()


@pytest.fixture
def create_loan(create_bank, create_customer):
    fake_nominal_value = round(
        fake.pydecimal(left_digits=5, right_digits=2, positive=True), 2
    )
    fake_interest_rate = round(
        fake.pydecimal(left_digits=1, right_digits=2, positive=True), 2
    )
    fake_request_date = fake.date_this_decade()
    fake_request_ip_address = fake.ipv4()

    return Loan.objects.create(
        nominal_value=fake_nominal_value,
        interest_rate=fake_interest_rate,
        request_date=fake_request_date,
        request_ip_address=fake_request_ip_address,
        bank=create_bank,
        customer=create_customer,
    )
