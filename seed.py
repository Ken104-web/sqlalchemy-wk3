from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
from models import Customer, Restaurant, Review, customer_restaurant

engine = create_engine('sqlite:///reviews3.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

if __name__ == '__main__':
    print('Begin DB....')
    session.query(Customer).delete()
    session.query(Restaurant).delete()
    session.query(Review).delete()
    print("Done")
    restaurant = []

    for i in range(10):
        new_customer = Customer(first_name=fake.name(),
        last_name=fake.last_name()
        )
        session.add(new_customer)
    print('customers counted')

    print('Now counting restaurants')
    for restaurant in range(7):
        restaurant = Restaurant(
            name=fake.company(),
            price=fake.random_int(min=1, max=7)

        )
        session.add(restaurant)

    for x in range(20):
        review = Review(
            star_rating=fake.random_int(min=1, max=5),
            customer_id=fake.random_int(min=1, max=10),  
            restaurant_id=fake.random_int(min=1, max=5)
        )
        session.add(review)
    print('print customer_restaurant')
    for i in session.query(Review).all():
        assign = customer_restaurant.insert().values(restaurant_id=i.restaurant_id, customer_id=i.customer_id)
        session.execute(assign)
        session.commit()

    print ('Reviews counted')
    # session.query(Customer).first().restaurants
    # session.query(Review).first().customer



        


    
    




    





