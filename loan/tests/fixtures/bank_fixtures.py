import pytest

from loan.models import Bank


@pytest.fixture
def create_bank():
    return Bank.objects.create(name="Banco do Brasil", code="001")
