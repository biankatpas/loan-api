import pytest

from loan.models import Customer


@pytest.fixture
def create_customer():
    return Customer.objects.create(
        name="Customer Name"
    )
