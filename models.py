from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///review.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
#  many to many
# creating table
customer_restaurant = Table('customer_restaurant', Base.metadata, Column('restaurant_id', ForeignKey('restaurant.id'), primary_key = True), Column('customer_id', ForeignKey('customer.id'), primary_key = True))

class Restaurants(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())

    #  one to many
    reviews = relationship('Review', backref=backref('restaurant'))
    # many to many with customers
    customers = relationship('Customer', secondary=customer_restaurant, back_populates='restaurant')

class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))

    # many to one relation
    customer = relationship('Customer', backref='reviews')


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer(), primary_key=True)
    first_name = (String())
    last_name = (String())


    restaurants = relationship('Restaurant', secondary=customer_restaurant, backref='customers')


    
    

