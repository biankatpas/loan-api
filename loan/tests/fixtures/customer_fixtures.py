import pytest
from faker import Faker

from loan.models import Customer
from loan.tests.fixtures.authentication_fixtures import create_user

fake = Faker()


@pytest.fixture
def create_customer(create_user):
    fake_user, _ = create_user
    return Customer.objects.create(name=fake.name(), user=fake_user)
