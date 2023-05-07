from backend.data_service.data_processors.base_measurement_processor import BaseMeasurementProcessor
from backend.data_service.models.measurement import Measurement


class ElectricityMeasurementProcessor(BaseMeasurementProcessor):
    def process(self, new_measurement_point: Measurement):
        self.measurement_storage["electricity_measurements"].append(new_measurement_point)
        print("Electricity data saved.")
