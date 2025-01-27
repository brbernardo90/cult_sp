from sqlalchemy import Column, Integer, String, Date, Text
from database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    unity = Column(String, nullable=True)
    type = Column(String, nullable=True)
    title = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    date = Column(String, nullable=True)  # Nullable to handle unparseable dates
    hour = Column(String, nullable=True)
    ticket = Column(String, nullable=True)
    location = Column(String, nullable=True)
