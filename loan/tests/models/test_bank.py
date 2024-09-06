import uuid

import pytest
from faker import Faker

from loan.models import Bank
from loan.tests.fixtures.bank_fixtures import create_bank

fake = Faker()


@pytest.mark.django_db
def test_bank_creation(create_bank):
    bank = create_bank

    expected_result = {"name": bank.name, "code": bank.code}

    assert isinstance(bank, Bank)
    assert isinstance(bank.id, uuid.UUID)
    assert bank.name == expected_result["name"]
    assert bank.code == expected_result["code"]


@pytest.mark.django_db
def test_bank_str(create_bank):
    bank = create_bank

    expected_result = bank.name

    assert str(bank) == expected_result


@pytest.mark.django_db
def test_bank_code_is_unique(create_bank):
    bank = create_bank

    with pytest.raises(Exception):
        Bank.objects.create(name=fake.company(), code=bank.code)
