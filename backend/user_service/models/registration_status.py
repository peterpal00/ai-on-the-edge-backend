from enum import Enum


class RegistrationStatus(Enum):
    INITIALIZATION = "initialization"
    REQUEST_CONFIRMATION = "request_confirmation"
    WAITING_FOR_CONFIRMATION = "waiting_for_confirmation"
    CONFIRMATION_SUCCESSFUL = "confirmation_successful"
    CONFIRMATION_FAILED = "confirmation_failed"
    CLOSED = "closed"

