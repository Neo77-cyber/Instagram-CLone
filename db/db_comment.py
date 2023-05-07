from fastapi import HTTPException, status
from schemas import CommentBase
from sqlalchemy.orm.session import Session
from db.models import DbComment
import datetime


def create(db: Session, request: CommentBase):
  new_comment = DbComment(
    text = request.text,
    username = request.username,
    post_id = request.post_id
  )
  db.add(new_comment)
  db.commit()
  db.refresh(new_comment)
  return new_comment

