import pytest
from faker import Faker

from loan.models import Bank

fake = Faker()


@pytest.fixture
def create_bank():
    return Bank.objects.create(name=fake.company(), code=fake.bothify(text="###"))
