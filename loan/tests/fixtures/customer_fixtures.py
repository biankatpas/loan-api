import pytest
from faker import Faker

from loan.models import Customer

fake = Faker()


@pytest.fixture
def create_customer():
    return Customer.objects.create(name=fake.name())
