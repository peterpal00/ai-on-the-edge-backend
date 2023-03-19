from typing import Any, Union

from fastapi import FastAPI

from backend.data_service.models.hardware_status import HardwareStatus
from backend.data_service.models.measurement import Measurement


def store_data(data: Union[Measurement, HardwareStatus]) -> Any:
    print("Data incoming:")
    print(data.json())


app = FastAPI()


@app.post("/measurement/")
def save_new_measurement_point(data: Measurement) -> Any:
    store_data(data=data)


@app.post("/hardware-status/")
async def save_new_hardware_status_point(data: HardwareStatus) -> Any:
    store_data(data=data)
