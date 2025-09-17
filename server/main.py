from fastapi import FastAPI, Depends, APIRouter
from services.db_session import engine, create_session
from models.todos import ToDo, Base
from routers.todo_router import router
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
@app.get("/")
def root():
    return {"message": "Hello To-Do"}