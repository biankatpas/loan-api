import pytest
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
def test_token_obtain_pair():
    client = APIClient()

    mock_username = "testuser"
    mock_password = "testpassword"

    _ = User.objects.create_user(username=mock_username, password=mock_password)

    response = client.post(
        "/api/token/",
        {
            "username": mock_username,
            "password": mock_password,
        },
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_token_does_not_obtain_pair():
    client = APIClient()

    mock_username = "testuser"
    mock_password = "testpassword"

    _ = User.objects.create_user(username=mock_username, password=mock_password)

    response = client.post(
        "/api/token/",
        {"username": mock_username, "password": "wrongpassword"},
        format="json",
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_token_refresh():
    client = APIClient()

    mock_username = "testuser"
    mock_password = "testpassword"

    user = User.objects.create_user(username=mock_username, password=mock_password)
    refresh = RefreshToken.for_user(user)

    response = client.post(
        "/api/token/refresh/", {"refresh": str(refresh)}, format="json"
    )

    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data


@pytest.mark.django_db
def test_token_does_not_refresh():
    client = APIClient()

    response = client.post(
        "/api/token/refresh/", {"refresh": "invalidtoken"}, format="json"
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
