from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class MeasurementType(Enum):
    WATER = "water"
    GAS = "gas"
    ELECTRICITY = "electricity"


class Measurement(BaseModel):
    value: str
    timestamp: str
    type: MeasurementType  # noqa: VNE003
    raw_value: Optional[str] = Field(alias="raw")
    previous_value: Optional[str] = Field(alias="pre")
    rate: Optional[str]
    error: Optional[str]
