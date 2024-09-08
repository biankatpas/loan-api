import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory

from loan.models import Customer
from loan.permissions import IsLoanOwner
from loan.tests.fixtures.payment_fixtures import (create_bank, create_customer,
                                                  create_loan, create_payment,
                                                  create_user)


@pytest.mark.django_db
def test_payment_owner_permission_granted(create_payment):
    payment = create_payment

    factory = APIRequestFactory()
    request = factory.get(f"/api/payments/{payment.id}/")
    request.user = payment.loan.customer.user

    permission = IsLoanOwner()

    has_permission = permission.has_object_permission(request, None, payment)

    assert has_permission


# TODO: test_payment_owner_permission_denied
