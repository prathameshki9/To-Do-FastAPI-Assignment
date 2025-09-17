from fastapi import Depends
from fastapi.responses import JSONResponse
from services.db_session import create_session
from models.todos import ToDo
from sqlalchemy.orm import Session

def get_todos(db: Session):
    data = db.query(ToDo).all()
    return JSONResponse(status_code=200, content={
        "status": "success",
        "message": "Todo's fetched successsfully",
        "data": data
    })