from influxdb import InfluxDBClient
from pydantic import BaseModel

from backend.data_service.models.measurement import Measurement


class BaseDataStore:
    def __init__(self, db_client: InfluxDBClient) -> None:
        self.db_client = db_client

    def save_data(self, data: BaseModel) -> None:
        self.db_client.write_points(data.json())

    def get_data_by_time(self, time: str) -> Measurement:
        raise NotImplementedError
