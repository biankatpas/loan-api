import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory

from loan.models import Customer
from loan.permissions import IsLoanOwner
from loan.tests.fixtures.loan_fixtures import (create_bank, create_customer,
                                               create_loan, create_user)


@pytest.mark.django_db
def test_loan_owner_permission_granted(create_loan):
    loan = create_loan

    factory = APIRequestFactory()
    request = factory.get(f"/api/loans/{loan.id}/")
    request.user = loan.customer.user

    permission = IsLoanOwner()

    has_permission = permission.has_object_permission(request, None, loan)

    assert has_permission


# TODO: test_loan_owner_permission_denied
