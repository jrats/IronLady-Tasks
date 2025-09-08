from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'           #connection string

#establish connection with an engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False} #multithread functionality
)

#each session will be a collection of transaction/ operations we perform on database
SessionLocal = sessionmaker(bind=engine, autoflush = False, autocommit=False)

Base = declarative_base()