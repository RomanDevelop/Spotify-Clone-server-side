from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

@app.post('/signup')
def signup_user(user: UserCreate):
    # extract the data thats coming from req
    print(user.name)
    print(user.email)
    print(user.password)
    # check if the user already exists in db
    # add the user to the db
    pass