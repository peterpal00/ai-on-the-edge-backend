from typing import Dict, Type

from backend.data_service.data_processors.base_measurement_processor import BaseMeasurementProcessor
from backend.data_service.data_processors.electricity_meausrement_processor import ElectricityMeasurementProcessor
from backend.data_service.data_processors.gas_measurement_processor import GasMeasurementProcessor
from backend.data_service.data_processors.water_measurement_processor import WaterMeasurementProcessor
from backend.data_service.models.measurement import MeasurementType

type_to_class_dict: Dict[MeasurementType, Type[BaseMeasurementProcessor]] = {
    MeasurementType.WATER: WaterMeasurementProcessor,
    MeasurementType.GAS: GasMeasurementProcessor,
    MeasurementType.ELECTRICITY: ElectricityMeasurementProcessor,
}


class DataProcessorFactory:
    def __init__(self, measurement_storage):
        self.measurement_storage = measurement_storage

    def get_processor(self, data_type: MeasurementType) -> BaseMeasurementProcessor:
        processor_class = type_to_class_dict[data_type]

        return processor_class(measurement_storage=self.measurement_storage)
