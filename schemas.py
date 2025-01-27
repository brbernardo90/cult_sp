from pydantic import BaseModel
from datetime import date

class Event(BaseModel):
    title: str
    location: str
    type: str
    description: str
    date: str

    class Config:
        orm_mode = True
