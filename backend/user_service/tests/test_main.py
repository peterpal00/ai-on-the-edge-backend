from unittest.mock import Mock, patch

from fastapi.testclient import TestClient
from fastapi import status

from backend.user_service.main import app
from backend.user_service.models.user_registration_model import UserRegistrationModel

test_client = TestClient(app)


@patch.object(UserRegistrationModel, 'set_id')
@patch.object(UserRegistrationModel, 'set_registration_code')
def test_hello(
        mock_user_registration_model_set_registration_code: Mock,
        mock_user_registration_model_set_id: Mock,
        test_first_name: str,
        test_last_name: str,
        test_birth_date: str,
        test_email_address: str,
        test_timestamp: str,
        test_uuid4_str: str,
        test_registration_code: str
):
    json_body = {
        "first_name": test_first_name,
        "last_name": test_last_name,
        "birth_date": test_birth_date,
        "email": test_email_address,
        "timestamp": test_timestamp,
    }

    expected_response = {
        "user_id": test_uuid4_str,
        "registration_code": test_registration_code
    }

    mock_user_registration_model_set_id.return_value = test_uuid4_str
    mock_user_registration_model_set_registration_code.return_value = test_registration_code

    response = test_client.post("/users/", json=json_body)

    assert response.status_code == status.HTTP_201_CREATED

    assert response.json() == expected_response
