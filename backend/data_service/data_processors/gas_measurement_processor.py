from backend.data_service.data_processors.base_measurement_processor import BaseMeasurementProcessor
from backend.data_service.models.measurement import Measurement


class GasMeasurementProcessor(BaseMeasurementProcessor):
    def process(self, new_measurement_point: Measurement) -> None:
        self.measurement_storage["gas_measurements"].append(new_measurement_point)
        print("Gas data saved.")
