import models, schemas, crud
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()


# dependency with the the DB
def get_db():
    db = SessionLocal()
    try:
        yield db   # will return when user hits endpoint
    finally:
        db.close()

# endpoints
# create an employee
@app.post('/employees', response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)


# get all employees
@app.get('/employees', response_model=List[schemas.EmployeeOut])
def get_employees(db: Session= Depends(get_db)):
    return crud.get_employees(db)

# get a specific employee
@app.get('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if not employee:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    return employee

# update an employee
@app.put('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def get_employee(emp_id: int, employee:schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id, employee)
    if not db_employee:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    return db_employee

# delete an employee
@app.delete('/employees/{emp_id}', response_model=dict)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)
    if not employee:
        raise HTTPException(status_code=404, detail='Employee Not Found')
    return {'detail':'Employee is deleted'}

