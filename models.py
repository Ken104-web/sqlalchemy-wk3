from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, ForeignKey

engine = create_engine('sqlite:///review.db')

Base = declarative_base()

class Restaurnats(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer(), primary_key=True)
    first_name = (String())
    last_name = (String())