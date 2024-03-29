import uuid
from typing import Optional

from pydantic import BaseModel, validator


class RegistrationConfirmationModel(BaseModel):
    registration_code: str

    @validator("registration_code", always=True)
    def check_if_uud4(cls, _var: str) -> Optional[str]:
        try:
            uuid.UUID(str(_var))
            return _var
        except ValueError:
            raise ValueError("Registration code is not uuid4.")
