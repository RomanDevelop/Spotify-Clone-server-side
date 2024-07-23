from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import TEXT, VARCHAR, Column, LargeBinary, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
import bcrypt

app = FastAPI()

DATABASE_URL = 'postgresql://postgres:1234@localhost:5432/musapp'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(TEXT, primary_key=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)

@app.post('/signup')
def signup_user(user: UserCreate):
    # extract the data thats coming from req

    # check if the user already exists in db
    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        raise HTTPException(400, 'User with the same email already exists!')
    
    hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4()), email=user.email, password=hashed_pw, name=user.name)
    # add the user to the db ________ 1.52.57
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db

Base.metadata.create_all(engine)