from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class CityBase(BaseModel):
    city: str

class CityCreate(CityBase):
    pass


class City(CityBase):

    city_id: int
    last_update: datetime
    country_id: int

    class Config:
        orm_mode = True

class CountryBase(BaseModel):
    country: str

class CountryCreate(CountryBase):
    pass

class Country(CountryBase):

    country_id: int
    last_update: datetime

    cities: List[City] = []

    class Config:
        orm_mode = True
