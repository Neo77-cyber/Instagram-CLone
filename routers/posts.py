from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas import PostBase, PostBaseDisplay, UserAuth
from db import db_post
from auth.oauth2 import get_current_user


router = APIRouter(prefix='/posts',
                   tags=['posts'])



@router.post('', response_model=PostBaseDisplay, )
def create(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
  
  return db_post.create(db, request)


