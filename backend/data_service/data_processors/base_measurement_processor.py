from abc import abstractmethod
from typing import Dict, List

from backend.data_service.models.measurement import Measurement


class BaseMeasurementProcessor:
    def __init__(self, measurement_storage: Dict[str, List]):
        self.measurement_storage = measurement_storage

    @abstractmethod
    def process(self, new_measurement_point: Measurement) -> None:
        pass
