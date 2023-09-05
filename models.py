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

class Restaurant(Base):

    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    price = Column(Integer())

    review = relationship('Review', backref=backref('restaurant_reviews'))

        # many to many with customers
    customer = relationship('Customer', secondary=customer_restaurant, back_populates='restaurant')


    def get_reviews(self):
        return self.reviews
    
    def all_customers(self):
        return self.customers
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    


class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))

    # many to one relation
    customer = relationship('Customer', backref=backref('review'))
    restaurant = relationship('Restaurants', backref=backref('review'))
   
    def get_customer(self):
        return self.customer
    
    def get_restaurant(self):
        return self.restaurant


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    # many to many  with customers
    restaurants = relationship('Restaurant', secondary=customer_restaurant, back_populates='customers')
    
    reviews = relationship('Review', back_populates='customer')
    

    def get_reviews(self):
        return self.reviews
    
    def all_restaurants(self):
        return self.restaurants
    
    def favorite_restaurant(self):
        
        customer_reviews = self.reviews

        highest_rating = 0
        fovorite_restaurant = None

        for review in customer_reviews:
            if review.star_rating > highest_rating:
                highest_rating = review.star_rating
                fovorite_restaurant = review.restaurant

        return fovorite_restaurant


    

    



    
    
    

