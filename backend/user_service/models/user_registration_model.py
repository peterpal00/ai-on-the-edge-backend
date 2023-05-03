from uuid import uuid4

from pydantic import BaseModel, validator

from backend.user_service.models.user_registration_status import UserRegistrationStatus


class UserRegistrationModel(BaseModel):
    user_id: str = None
    first_name: str
    last_name: str
    birth_date: str
    email: str
    timestamp: str
    registration_status: UserRegistrationStatus = None
    registration_code: str = None

    @validator("user_id", pre=True, always=True)
    def set_id(cls, _var):
        return str(uuid4())

    @validator("registration_code", always=True)
    def set_registration_code(cls, _var):
        return str(uuid4())

    @validator("registration_status", always=True)
    def set_init_registrations_status(cls, _var):
        return UserRegistrationStatus.PENDING

    def set_registration_to_completed(self):
        self.registration_status = UserRegistrationStatus.COMPLETED

    def is_user_in_registration_pending(self):
        return self.registration_status == UserRegistrationStatus.PENDING
