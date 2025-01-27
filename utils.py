import json
from sqlalchemy.orm import Session
from models import Event
from datetime import datetime

def parse_date(date_str):
    # Custom function to handle date parsing
    try:
        # Handle specific date formats as needed
        return datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        return None  # Return None for invalid or unparseable dates

def load_data_from_json(file_path: str, db: Session):
    with open(file_path, encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)

        for unit in data:
            unity = unit.get("unity", "Unknown Unity")
            events = unit.get("events", [])
            type = 'musica'

            for event in events:
                date = event.get("date", "Não informado")
                # For simplicity, assume we're storing only the first parsed date
                # parsed_date = parse_date(date.split(",")[0].strip()) if date != "Não informado" else None

                # Insert each event into the database
                new_event = Event(
                    unity=unity,
                    title=event["title"],
                    type=type,
                    location=event.get("local", "Não informado"),
                    description=event.get("description", "Sem descrição"),
                    date=date,
                    hour=event["hour"],
                    ticket=event["ticket"],
                )
                db.add(new_event)
        db.commit()
