import pytest
from django.contrib.auth.models import User
from faker import Faker
from rest_framework.test import APIClient

faker = Faker()


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def create_user():
    fake_password = faker.password()
    fake_user = User.objects.create_user(
        username=faker.user_name(), password=fake_password
    )
    return fake_user, fake_password
