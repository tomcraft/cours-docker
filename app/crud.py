from sqlalchemy.orm import Session

import models, dto


def get_country(db: Session, country_id: int):
    return db.query(models.Country).filter(models.Country.country_id == country_id).first()


def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Country).offset(skip).limit(limit).all()


def create_country(db: Session, country: dto.CountryCreate):
    db_country = models.Country(country=country.country)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country


def get_cities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.City).offset(skip).limit(limit).all()


def create_country_city(db: Session, city: dto.CityCreate, country_id: int):
    db_city = models.City(**city.dict(), country_id=country_id)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city
