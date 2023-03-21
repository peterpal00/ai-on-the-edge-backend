from fastapi import FastAPI

from backend.user_service.models.user_registration_model import UserRegistrationModel

app = FastAPI()

@app.post("/user-registration/")
def register_user(data: UserRegistrationModel):
