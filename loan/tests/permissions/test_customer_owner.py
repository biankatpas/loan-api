import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory

from loan.models import Loan
from loan.permissions import IsCustomerOwner
from loan.tests.fixtures.customer_fixtures import create_customer, create_user


@pytest.mark.django_db
def test_customer_owner_permission_granted(create_customer):
    customer = create_customer

    factory = APIRequestFactory()
    request = factory.get(f"/api/customers/{customer.id}/")
    request.user = customer.user

    permission = IsCustomerOwner()

    has_permission = permission.has_object_permission(request, None, customer)

    assert has_permission


# TODO: test_customer_owner_permission_denied
