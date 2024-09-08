import pytest
from rest_framework import status

from loan.models import Customer
from loan.tests.fixtures.authentication_fixtures import client
from loan.tests.fixtures.customer_fixtures import create_customer, create_user


@pytest.mark.django_db
def test_customer_list_view_authenticated(create_customer, client):
    customer = create_customer

    api_client = client
    api_client.force_authenticate(user=customer.user)

    response = api_client.get("/api/customers/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0


@pytest.mark.django_db
def test_customer_list_view_unauthenticated(client, create_customer):
    api_client = client

    response = api_client.get("/api/customers/")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_customer_create_view(client, create_user):
    user, _ = create_user

    api_client = client
    api_client.force_authenticate(user=user)

    data = {
        "name": "Customer Name",
    }

    response = client.post("/api/customers/", data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Customer.objects.count() == 1
    assert Customer.objects.get().user == user


# TODO: test CustomerRetrieveUpdateDestroyAPIView
