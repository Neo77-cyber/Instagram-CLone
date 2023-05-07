from fastapi import FastAPI
from routers import user, posts, comments
from db import models
from db.database import engine
from auth import authentication


app = FastAPI()

app.include_router(user.router)
app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(authentication.router)


models.Base.metadata.create_all(engine)

