from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models
from app.database import engine
from .routers import post, user, auth,Likes
from app.config import settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(Likes.router)


@app.get("/")
def root():
    return{"message": "Refer to the docs to know more about the api"}