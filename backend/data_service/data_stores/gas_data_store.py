from influxdb import InfluxDBClient

from backend.data_service.data_stores.base_data_store import BaseDataStore


class GasDataStore(BaseDataStore):
    def __init__(self, db_client: InfluxDBClient):
        super().__init__(db_client)

        self.db_client.switch_database("gas_meter_readings")
