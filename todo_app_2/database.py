from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, Boolean, String


database_url = "sqlite:///todos.db"
engine = create_engine(database_url, connect_args={'check_same_thread': False})

Base = declarative_base()


class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)