# all imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# database location
SQLALCHEMY_DATABASE_URL = "sqlite:///todos.db"

# creating the engine by using create_engine function
# connect argument is to make sure the sqlite database not to check the same thread all the time
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})


# creating a Session of the database
# don't want automatic commit to the database
# don't want automatic flush to the database
# also binding to the engine object
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative base is for inherit the sqlalchemy table object that will convert to a sql table later
Base = declarative_base()


