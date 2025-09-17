from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TodoPyModel(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    due_date: datetime
    priority: int

class UpdateTodoPyModel(BaseModel):
    id: Optional[int]
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]
    due_date: Optional[datetime]
    priority: Optional[int] 