from sqlalchemy import Column, Integer, String, ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=Integer, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    posts = relationship("DbPost", back_populates='user')

class DbPost(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=Integer, index=True)
    image = Column(String)
    caption = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("DbUser", back_populates='posts')

    comments = relationship("DbComment", back_populates="post_items")



class DbComment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=Integer, index=True)
    text = Column(String)
    username = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))

    post_items = relationship("DbPost", back_populates="comments")





    