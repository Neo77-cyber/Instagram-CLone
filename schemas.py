from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str
    

class UserBaseDisplay(BaseModel):
    username: str
    email: str
    class Config():
        orm_mode = True


class User(BaseModel):
    username: str
    class Config():
        orm_mode = True

class Comment(BaseModel):
    text: str
    username: str
    class Config():
        orm_mode = True


class PostBase(BaseModel):
    image: str
    caption: str
    creator_id: int

class PostBaseDisplay(BaseModel):
    id: int 
    image: str
    caption: str
    user: User
    comments: list[Comment]
    class Config():
        orm_mode = True

class CommentBase(BaseModel):
    text: str
    username: str
    post_id: int

class UserAuth(BaseModel):
  id: int
  username: str
  email: str








