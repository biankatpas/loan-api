import pytest
from rest_framework import status

from loan.tests.fixtures.authentication_fixtures import client
from loan.tests.fixtures.loan_fixtures import (create_bank, create_customer,
                                               create_loan, create_user)


@pytest.mark.django_db
def test_loan_list_view_authenticated(create_loan, client):
    loan = create_loan

    api_client = client
    api_client.force_authenticate(user=loan.customer.user)

    response = client.get("/api/loans/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0
    assert response.data[0]["customer"]["id"] == str(loan.customer.id)


@pytest.mark.django_db
def test_loan_list_view_unauthenticated(client):
    api_client = client

    response = api_client.get("/api/loans/")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


# TODO: test LoanRetrieveUpdateDestroyAPIView
