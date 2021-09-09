from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP, DateTime

from database import Base

class Country(Base):

    __tablename__ = "country"


    country_id = Column(Integer, primary_key=True, index=True)
    country = Column(String, unique=True, index=True)
    last_update = Column(DateTime)

    cities = relationship("City", back_populates="country")



class City(Base):

    __tablename__ = "city"


    city_id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    country_id = Column(Integer, ForeignKey("country.country_id"))
    last_update = Column(DateTime)

    country = relationship("Country", back_populates="cities")
