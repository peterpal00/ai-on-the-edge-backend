from fastapi import FastAPI, status

from backend.data_service.data_processors.data_processor_factory import DataProcessorFactory
from backend.data_service.models.measurement import Measurement

data_points = dict(water_measurements=list(), gas_measurements=list(), electricity_measurements=list())

measurement_processor_factory = DataProcessorFactory(measurement_storage=data_points)

app = FastAPI()


@app.post("/data/", status_code=status.HTTP_201_CREATED)
async def save_measurement_point(data_point: Measurement):

    processor = measurement_processor_factory.get_processor(data_type=data_point.type)
    processor.process(data_point)

    return data_point.dict()
