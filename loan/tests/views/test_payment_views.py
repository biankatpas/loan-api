import pytest
from rest_framework import status

from loan.tests.fixtures.authentication_fixtures import client
from loan.tests.fixtures.payment_fixtures import (create_bank, create_customer,
                                                  create_loan, create_payment,
                                                  create_user)


@pytest.mark.django_db
def test_payment_list_view_authenticated(create_payment, client):
    payment = create_payment

    api_client = client
    api_client.force_authenticate(user=payment.loan.customer.user)

    response = client.get("/api/payments/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0
    assert response.data[0]["loan"]["id"] == str(payment.loan.id)


@pytest.mark.django_db
def test_payment_list_view_unauthenticated(client):
    api_client = client

    response = api_client.get("/api/payments/")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


# TODO: test PaymentRetrieveUpdateDestroyAPIView
