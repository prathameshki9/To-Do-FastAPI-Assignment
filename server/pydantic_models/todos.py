from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TodoPyModel(BaseModel):
    title: str
    description: Optional[str] = ""
    completed: bool
    due_date: datetime
    priority: int

class UpdateTodoPyModel(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None
    priority: Optional[int]  = None