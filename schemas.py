from pydantic import BaseModel

class TaskBase(BaseModel):
    title:str
    description:str | None = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id:int
    completed:bool


class TaskUpdate(BaseModel):
    title:str | None = None
    description:str | None=None
    completed: bool | None = None

    class Config:
        from_attribute = True # ✅ Allows Pydantic to create this model from ORM (e.g., SQLAlchemy) objects
                             # by reading their attributes directly and converting them into the
                             # Pydantic model structure for JSON responses in FastAPI.
                             #
                             # This replaces `orm_mode = True` in Pydantic V1 and is required in V2.
                             #
                             # Without this, Pydantic expects a dict, not an ORM instance.