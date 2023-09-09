# SQLAlchemy Challenge

This project aims at understanding concepts on 
- SQLalchemy Migrations,
- SQLAlchemy Relationships Class
- Instance Methods 
- SQLAlchemy Querying

#  Clone the Repository

You can clone the repo using the link provided:

```https://github.com/Ken104-web/sqlalchemy-wk3```

Use the Pipefile to install dependancies for this project.

Run the following command in your Terminal.

```bash  pipenv install```

# Deliverables

We are building three models namels `Customer`,    `Restaurant`,   `Reviews`

The application of object relationship methods was applied here through the deliverables described.

 #  Review
- `Review customer()`

 - should return the `Customer` instance for this review

- `Review restaurant()`

 - should return the `Restaurant` instance for this review

 

# Restaurant
 

- `Restaurant reviews()`

 - returns a collection of all the reviews for the `Restaurant`

- `Restaurant customers()`

 - returns a collection of all the customers who reviewed the `Restaurant`

 

 # Customer
 

- `Customer reviews()`

 - should return a collection of all the reviews that the `Customer` has left

- `Customer restaurants()`

 - should return a collection of all the restaurants that the `Customer` has reviewed.


Others methods applied include: Aggregate and Relationship Methods where

 #  Customer
 

- `Customer full_name()`

 - returns the full name of the customer, with the first name and the last name  concatenated, Western style.

- `Customer favorite_restaurant()`

 - returns the restaurant instance that has the highest star rating from this customer

- `Customer add_review(restaurant, rating)`

 - takes a `restaurant` (an instance of the `Restaurant` class) and a rating

 - creates a new review for the restaurant with the given `restaurant_id`

- `Customer delete_reviews(restaurant)`

 - takes a `restaurant` (an instance of the `Restaurant` class) and

 - removes all their reviews for this restaurant

 - you will have to delete rows from the `reviews` table to get this to work!

 

# Review
- `Review full_review()`

 - should return a string formatted as follows:
Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.

# technologies used
python

sqlalchemy

# Author

Kenneth Mwangi




