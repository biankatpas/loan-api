import pytest
from rest_framework import status
from rest_framework.exceptions import ValidationError

from loan.serializers import LoanCreateSerializer, LoanDetailSerializer
from loan.tests.fixtures.loan_fixtures import (create_bank, create_customer,
                                               create_loan, create_user)

# TODO: tests for the new loan serializers

# @pytest.mark.django_db
# def test_loan_serializer_valid_data(create_loan):
#     loan = create_loan

#     serializer = LoanSerializer(instance=loan)

#     assert serializer.data["nominal_value"] == str(loan.nominal_value)
#     assert serializer.data["interest_rate"] == str(loan.interest_rate)
#     assert serializer.data["request_ip_address"] == loan.request_ip_address
#     assert serializer.data["bank"] == loan.bank.id
#     assert serializer.data["customer"] == loan.customer.id


# @pytest.mark.django_db
# def test_loan_serializer_invalid_data(create_loan):
#     loan = create_loan

#     mock_invalid_data = {
#         "nominal_value": "not_a_number",
#         "interest_rate": loan.interest_rate,
#         "request_date": loan.request_date,
#         "request_ip_address": loan.request_ip_address,
#         "bank": 1,
#         "customer": 1,
#     }

#     serializer = LoanSerializer(data=mock_invalid_data)

#     assert not serializer.is_valid()
#     assert "nominal_value" in serializer.errors
