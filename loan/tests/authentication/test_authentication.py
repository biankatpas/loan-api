import pytest
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from loan.tests.fixtures.authentication_fixtures import client, create_user


@pytest.mark.django_db
def test_token_obtain_pair(client, create_user):
    user, password = create_user

    response = client.post(
        "/api/token/",
        {
            "username": user.username,
            "password": password,
        },
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_token_does_not_obtain_pair(client, create_user):
    user, _ = create_user

    response = client.post(
        "/api/token/",
        {"username": user.username, "password": "wrongpassword"},
        format="json",
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_token_refresh(client, create_user):
    user, _ = create_user
    refresh = RefreshToken.for_user(user)

    response = client.post(
        "/api/token/refresh/", {"refresh": str(refresh)}, format="json"
    )

    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data


@pytest.mark.django_db
def test_token_does_not_refresh(client):
    response = client.post(
        "/api/token/refresh/", {"refresh": "invalidtoken"}, format="json"
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
