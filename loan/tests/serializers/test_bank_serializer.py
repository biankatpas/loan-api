import pytest

from rest_framework.exceptions import ValidationError

from loan.serializers import BankSerializer
from loan.tests.fixtures.bank_fixtures import create_bank


@pytest.mark.django_db
def test_bank_serializer_valid_data(create_bank):
    bank = create_bank

    serializer = BankSerializer(instance=bank)

    assert serializer.data['name'] == bank.name
    assert serializer.data['code'] == bank.code
    assert serializer.data['id'] == str(bank.id)


@pytest.mark.django_db
def test_bank_serializer_invalid_data():
    mock_invalid_data = {
        'name': '',
        'code': '',
    }

    serializer = BankSerializer(data=mock_invalid_data)

    assert not serializer.is_valid()
    assert 'name' in serializer.errors
    assert 'code' in serializer.errors
