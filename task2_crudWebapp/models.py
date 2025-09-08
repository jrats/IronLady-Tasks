#defining the structure of our table using a class

from sqlalchemy import Column, Integer, String
from database import Base

# Employee Model for basic CRUD operations
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    feedback = Column(String, nullable=True) #sentiment of the feedback will be gauged
    sentiment = Column(String, nullable=True)



