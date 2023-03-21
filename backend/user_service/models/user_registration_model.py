from uuid import uuid4

from pydantic import BaseModel, validator


class UserRegistrationModel(BaseModel):
    id: str = None
    first_name: str
    last_name: str
    birth_date: str
    email: str
    timestamp: str

    @validator('id', pre=True, always=True)
    def set_id(cls, v):
        return v or str(uuid4())
