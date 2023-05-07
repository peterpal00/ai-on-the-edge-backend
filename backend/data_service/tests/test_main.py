from fastapi import status
from fastapi.testclient import TestClient

from backend.data_service.main import app
from backend.data_service.models.measurement import MeasurementType

test_client = TestClient(app)


def test_save_water_measurement(
    test_value: str, test_raw: str, test_pre: str, test_error: str, test_rate: str, test_timestamp: str
):
    json_body = {
        "value": test_value,
        "raw": test_raw,
        "pre": test_pre,
        "error": test_error,
        "rate": test_rate,
        "timestamp": test_timestamp,
        "type": MeasurementType.WATER.value,
    }

    response = test_client.post("/data/", json=json_body)

    assert response.status_code == status.HTTP_201_CREATED


def test_save_gas_measurement(
    test_value: str, test_raw: str, test_pre: str, test_error: str, test_rate: str, test_timestamp: str
):
    json_body = {
        "value": test_value,
        "raw": test_raw,
        "pre": test_pre,
        "error": test_error,
        "rate": test_rate,
        "timestamp": test_timestamp,
        "type": MeasurementType.GAS.value,
    }

    response = test_client.post("/data/", json=json_body)

    assert response.status_code == status.HTTP_201_CREATED


def test_save_electricity_measurement(
    test_value: str, test_raw: str, test_pre: str, test_error: str, test_rate: str, test_timestamp: str
):
    json_body = {
        "value": test_value,
        "raw": test_raw,
        "pre": test_pre,
        "error": test_error,
        "rate": test_rate,
        "timestamp": test_timestamp,
        "type": MeasurementType.ELECTRICITY.value,
    }

    response = test_client.post("/data/", json=json_body)

    assert response.status_code == status.HTTP_201_CREATED
