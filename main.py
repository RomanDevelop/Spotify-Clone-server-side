from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

DATABASE_URL = 'postgresql://postgres:123Test@localhost:5432/flutternellimusicapp'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

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