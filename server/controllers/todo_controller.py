from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
from services.db_session import create_session
from models.todos import ToDo
from sqlalchemy.orm import Session
from pydantic_models.todos import TodoPyModel, UpdateTodoPyModel

def get_todos(db: Session):
    data = db.query(ToDo).all()
    return {"status": "success", "message": "Todos fethed successfully","data": data}

def add_todo(db: Session, todo: TodoPyModel):
    todo_exists = db.query(ToDo).filter(ToDo.title == todo.title).filter(ToDo.description == todo.description).first()
    
    if todo_exists:
        raise HTTPException(status_code=400, detail="Todo item with title and description already exists")
    
    data = todo.model_dump()
    print(data)
    db.add(ToDo(**data))
    db.commit()
    return JSONResponse(status_code=200, content={
        "status": "success",
        "message": "ToDo item added"
    })

def update_todo(db: Session, todo: UpdateTodoPyModel, id: int):
    todo_present = db.query(ToDo).filter(ToDo.id == id).first()
    if not todo_present:
        raise HTTPException(status_code=400, detail="ToDo item does not exists")
    
    if todo.title is not None:
        todo_present.title = todo.title
    if todo.description is not None:
        todo_present.description = todo.description
    if todo.completed is not None:
        todo_present.completed = todo.completed
    if todo.due_date is not None:
        todo_present.due_date = todo.due_date
    if todo.priority is not None:
        todo_present.priority = todo.priority

    db.commit()
    return JSONResponse(status_code=200, content={
        "status": "success",
        "message": "Todo item updated successfully"
    })

def delete_todo(db: Session, id: int):
    todo_present = db.query(ToDo).filter(ToDo.id == id).first()

    if not todo_present:
        raise HTTPException(status_code=400, detail="Todo item not present")

    db.delete(todo_present)
    db.commit()

    return JSONResponse(status_code=200, content={
        "status": "success",
        "message": "Todo item deleted successfully"
    })