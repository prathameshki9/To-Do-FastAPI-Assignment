from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ToDo(Base):

    __tablename__ = "todo"

    id= Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500))
    completed = Column(Boolean, default=False, index=True)
    due_date = Column(DateTime, index=True)
    priority = Column(Integer, default=3)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, index=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False, index=True)