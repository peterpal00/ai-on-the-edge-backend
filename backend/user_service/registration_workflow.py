from transitions import Machine

from backend.user_service.models.registration_status import RegistrationStatus


class RegistrationWorkflow:

    def __init__(self):
        self.state_machine = Machine(model=self,states=RegistrationStatus, initial=RegistrationStatus.INITIALIZATION)

        self.state_machine.add_transition(
            trigger="to_request_confirmation",
            source=RegistrationStatus.INITIALIZATION,
            dest=RegistrationStatus.REQUEST_CONFIRMATION
        )

        self.state_machine.add_transition(
            trigger="to_waiting_confirmation",
            source=RegistrationStatus.REQUEST_CONFIRMATION,
            dest=RegistrationStatus.WAITING_FOR_CONFIRMATION
        )

        self.state_machine.add_transition(
            "to_confirmation_successful",
            source=RegistrationStatus.WAITING_FOR_CONFIRMATION,
            dest=RegistrationStatus.CONFIRMATION_SUCCESSFUL,
        )

        self.state_machine.add_transition(
            trigger="to_confirmation_failed",
            source=RegistrationStatus.WAITING_FOR_CONFIRMATION,
            dest=RegistrationStatus.CONFIRMATION_FAILED,
        )

        self.state_machine.add_transition(
            trigger="to_closed",
            source=[
                RegistrationStatus.CONFIRMATION_SUCCESSFUL,
                RegistrationStatus.CONFIRMATION_FAILED
                ],
            dest=RegistrationStatus.CLOSED,
        )

