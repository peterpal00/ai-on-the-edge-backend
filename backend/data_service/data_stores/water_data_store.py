from influxdb import InfluxDBClient

from backend.data_service.data_stores.base_data_store import BaseDataStore


class WaterDataStore(BaseDataStore):
    def __init__(self, db_client: InfluxDBClient):
        super().__init__(db_client)

        self.db_client.switch_database("water_meter_readings")
