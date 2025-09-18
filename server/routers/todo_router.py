from fastapi import APIRouter, Depends
from controllers.todo_controller import get_todos, add_todo, update_todo, delete_todo
from sqlalchemy.orm import Session
from services.db_session import create_session
from pydantic_models.todos import TodoPyModel, UpdateTodoPyModel

router = APIRouter(tags=["ToDo"])

@router.get("/todo")
def get_todos_router(db: Session = Depends(create_session)):
    return get_todos(db)

@router.post("/todo")
def add_todo_router(*, db: Session = Depends(create_session), todo: TodoPyModel):
    return add_todo(db, todo)

@router.put("/todo/{id}")
def update_todo_router(*, db: Session = Depends(create_session), todo: UpdateTodoPyModel ,id: int):
    return update_todo(db, todo, id)

@router.delete("/todo/{id}")
def delete_todo_router(*, db: Session = Depends(create_session), id: int):
    return delete_todo(db, id)