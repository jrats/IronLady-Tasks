from pydantic import BaseModel, EmailStr
from typing import Optional

# id is an auto generated field and will not be included in this class

# Employee Schema
class EmployeeBase(BaseModel):
    name : str
    email : EmailStr
    feedback: Optional[str] = None

class EmployeeCreate(EmployeeBase):
    pass 

class EmployeeUpdate(EmployeeBase):
    pass 

class EmployeeOut(EmployeeBase):     #read employee data
    id : int 
    sentiment : Optional[str] = None

    class Config:
        orm_mode = True



