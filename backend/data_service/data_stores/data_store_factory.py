from typing import Type

from influxdb import InfluxDBClient

from backend.data_service.data_stores.base_data_store import BaseDataStore
from backend.data_service.data_stores.electricity_data_store import ElectricityDataStorage
from backend.data_service.data_stores.gas_data_store import GasDataStore
from backend.data_service.data_stores.water_data_store import WaterDataStore
from backend.data_service.models.measurement import MeasurementType

type_to_class_mapping = {
    MeasurementType.GAS: GasDataStore,
    MeasurementType.WATER: WaterDataStore,
    MeasurementType.ELECTRICITY: ElectricityDataStorage,
}


class DataStoreFactory:
    def __init__(self, db_client: InfluxDBClient) -> None:

        self.db_client = db_client

    def get_data_store(self, data_type: MeasurementType) -> BaseDataStore:
        data_store_type: Type[BaseDataStore] = type_to_class_mapping[data_type]

        return data_store_type(db_client=self.db_client)
