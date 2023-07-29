# all imports
import models
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from database import engine, SessionLocal


# declaring the fastapi application
app = FastAPI()


models.Base.metadata.create_all(bind=engine)


# dependency injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# all routing functions
@app.get('/')
async def read_all(db: Annotated[Session, Depends(get_db)]):  # injected dependency of the database using Depends from FastApi
    return db.query
