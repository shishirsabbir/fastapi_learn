from sqlalchemy.orm import Session
from database import Base, SessionLocal, Todos, engine


Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()