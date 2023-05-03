from typing import Dict

from fastapi import FastAPI, HTTPException, status

from backend.user_service.models.registration_confirmation_model import RegistrationConfirmationModel
from backend.user_service.models.user_registration_model import UserRegistrationModel

app = FastAPI()

users: Dict[str, UserRegistrationModel] = dict()


@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def root(user: UserRegistrationModel):

    users.update({user.user_id: user})
    for val in users.values():
        print(val)

    return {"user_id": user.user_id, "registration_code": user.registration_code}


@app.post("/users/{user_id}/registration-confirmation/", status_code=status.HTTP_202_ACCEPTED)
def registration_confirmation(user_id: str, registration_confirmation: RegistrationConfirmationModel):
    try:
        user = users[user_id]
    except Exception:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="The given user id doesn't exist.")

    if not user.is_user_in_registration_pending():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Registration is not in pending status."
        )
    if user.registration_code != registration_confirmation.registration_code:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Registration code is wrong.")

    user.set_registration_to_completed()

    return user.dict()
