from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

host = os.environ['MYSQL_HOST']
port = os.environ['MYSQL_PORT']
user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
db = os.environ['MYSQL_DB']

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(user, password, host, port, db)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
