from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas import UserBase, UserBaseDisplay
from db import db_user


router = APIRouter(prefix='/users',
                   tags=['users'])



@router.post('/signup', response_model=UserBaseDisplay)
def signup(request: UserBase,  db:Session = Depends(get_db)):
    return db_user.create_user(db, request)


