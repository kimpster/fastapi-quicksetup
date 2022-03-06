from fastapi import FastAPI
from . import models
from .database import engine
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# To run the api on localhost: uvicorn app.main:app --reload

app = FastAPI()

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  Example routes app.include_router(post.router)

@app.get("/")
async def root():
    return {"message": "Welcome to my api!"}


