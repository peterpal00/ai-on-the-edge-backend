from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class MeasurementType(Enum):
    WATER = 1
    GAS = 2
    ELECTRICITY = 3


measurement_types: dict = {
    "water": MeasurementType.WATER,
    "gas": MeasurementType.GAS,
    "electricity": MeasurementType.ELECTRICITY,
}


class Measurement(BaseModel):
    value: str
    timestamp: str
    type: str  # noqa: VNE003
    raw_value: Optional[str] = Field(alias="raw")
    previous_value: Optional[str] = Field(alias="pre")
    rate: Optional[str]
    error: Optional[str]
