import uuid

import pytest

from loan.models import Bank
from loan.tests.fixtures.bank_fixtures import create_bank


@pytest.mark.django_db
def test_bank_creation(create_bank):
    bank = create_bank

    expected_result = {"name": "Banco do Brasil", "code": "001"}

    assert isinstance(bank, Bank)
    assert isinstance(bank.id, uuid.UUID)
    assert bank.name == expected_result["name"]
    assert bank.code == expected_result["code"]


@pytest.mark.django_db
def test_bank_str(create_bank):
    bank = create_bank
    assert str(bank) == "Banco do Brasil"


@pytest.mark.django_db
def test_bank_code_is_unique(create_bank):
    with pytest.raises(Exception):
        Bank.objects.create(name="Other Bank Name", code="001")
