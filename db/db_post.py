from fastapi import HTTPException, status
from schemas import PostBase
from sqlalchemy.orm.session import Session
from db.models import DbPost
import datetime


def create(db: Session, request: PostBase):
  new_post = DbPost(
    image = request.image,
    caption = request.caption,
    user_id = request.creator_id
  )
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post

