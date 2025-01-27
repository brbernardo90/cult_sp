from sqlalchemy.orm import Session
from models import Event
from datetime import date

def get_all_events(db: Session):
    return db.query(Event).all()

def get_upcoming_events(db: Session):
    return db.query(Event).filter(Event.date >= date.today()).all()
