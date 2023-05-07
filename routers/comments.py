from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas import CommentBase, UserAuth
from db import db_comment
from auth.oauth2 import get_current_user


router = APIRouter(prefix='/comments',
                   tags=['comments'])



@router.post('')
def create(request: CommentBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
  
  return db_comment.create(db, request)


