from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud, models, dto
from database import SessionLocal, engine
import uvicorn
import json

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/countries", response_model=dto.Country)
def create_country(country: dto.CountryCreate, db: Session = Depends(get_db)):
    return crud.create_country(db=db, country=country)


@app.get("/countries", response_model=List[dto.Country])
def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_countries(db, skip=skip, limit=limit)


@app.get("/countries/{country_id}", response_model=dto.Country)
def read_country(country_id: int, db: Session = Depends(get_db)):
    db_country = crud.get_country(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country


@app.get("/countries/{country_id}/cities", response_model=List[dto.City])
def create_country_city(country_id: int, db: Session = Depends(get_db)):
    db_country = crud.get_country(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country.cities
    

@app.post("/countries/{country_id}/cities", response_model=dto.City)
def create_country_city(country_id: int, city: dto.CityCreate, db: Session = Depends(get_db)):
    db_country = crud.get_country(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return crud.create_country_city(db, country_id=country_id, city=city)


@app.get("/status")
async def status():
    return {"status": "Running"}