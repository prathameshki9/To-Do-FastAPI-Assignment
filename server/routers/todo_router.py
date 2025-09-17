from fastapi import APIRouter, Depends
from controllers.todo_controller import get_todos
from sqlalchemy.orm import Session
from services.db_session import create_session

router = APIRouter(tags=["ToDo"])

@router.get("/todo")
def get_todos_router(db: Session = Depends(create_session)):
    return get_todos(db)

