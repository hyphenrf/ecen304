from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_

from datetime import datetime
from datetime import timedelta

db = SQLAlchemy()

# all classes inherit from db.Model. This allows for the class to have some built-in relationship with SQLAlchemy to interact with the database.
#__str__ is the built-in function in python, used in classes for string representation of object.

# -------------------    Books  ----------------------# #----1----#


class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key =  True)
    isbn = db.Column(db.String, unique = True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"), nullable=False)
    year = db.Column(db.Integer, db.CheckConstraint('year <= 2020') ,nullable=False)
    total = db.Column(db.Integer, nullable=False)
    sold = db.Column(db.Integer, default = 0 ,nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __str__(self):
        return f"{self.title} by {self.author} for ({self.price} EGP) ({self.total}) Copies."

    # EditBook_Num edits the price and total number of copies for a book
    def EditBook_Num(self, total,price):     
        self.total = total
        self.price = price
        db.session.commit()
    
    # Sell_Copy decreases total number of copies for a book by 1 and increase sold number by 1 when a copy is sold. It raises an Exception if there are no available copies.
    def Sell_Copy(self):
        if (total >0):    
            self.total -= 1
            self.sold += 1
            db.session.commit()
        
        else:
            raise Exception('Book is not available for the time being.')

    # Return_Copy increases total number of copies for a book by 1 and decreases sold number by 1 when a copy is returned. 
    def Return_Copy(self):     
        self.total += 1
        self.sold -= 1
        db.session.commit()

    # OrderBook  creates an object from Orders class, adds it to the database, and calls Sell_Copy method.
    def OrderBook(self,user_id):
        today = datetime.now()        
        new_order = Orders(user_id = user_id, book_id = self.id, order_time = today)
        self.Sell_Copy()
        db.session.add(new_order)
        db.session.commit()

    # RateBook created an object from Ratings class and adds it to the database. It rasies an exception if the user has a rating in the database already.
    def RateBook(self, user_id, rating):
        rating_count = Ratings.query.filter(and_(Ratings.user_id == user_id , Ratings.book_id == self.id)).count()
        if rating_count == 0:
            rating = Ratings(rating = rating, user_id = user_id, book_id = self.id)
            db.session.add(rating)
            db.session.commit()
        else:
            raise Exception('User Already has a rating. EditRate instead.')

    # ReviewBook created an object from Reviews class and adds it to the database. It rasies an exception if the user has a review in the database already.
    def ReviewBook(self, user_id, review):
        review_count = Reviews.query.filter(and_(Reviews.user_id == user_id , Reviews.book_id == self.id)).count()
        if review_count > 0:
            review = Reviews(review = review, user_id = user_id, book_id = self.id)
            db.session.add(review)
            db.session.commit()
        else:
            raise Exception('User Already has a review. EditReview instead.')

    # EditRate edits a user's rating. It rasies an exception if the user doesn't have a rating in the database already.
    def EditRate(self, user_id, rating):
        myrating = Ratings.query.filter(and_(Ratings.user_id == user_id , Ratings.book_id == self.id)).first()
        if myrating != None:
            myrating.rating = rating
            db.session.commit()
        else:
            raise Exception('User does not have a rating. RateBook instead.')

    # EditReview edits a user's review. It rasies an exception if the user doesn't have a review in the database already.
    def EditReview(self, user_id, review):
        myreview = Reviews.query.filter(and_(Reviews.user_id == user_id , Reviews.book_id == self.id)).first()
        if myreview != None:
            myreview.review = review
            db.session.commit()
        else:
            raise Exception('User does not have a review. ReviewBook instead.')


# -------------------    Ratings  ----------------------# #----2----#

class Ratings(db.Model):
    __tablename__ = "ratings"
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, db.CheckConstraint('0 <= rating AND rating <= 5') ,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)

    def __str__(self):
        return f"user with id ({self.user_id}) rated {self.rating} for book with id ({self.book_id})"

    # EditRate edits a user's rating. 
    def EditRate(self, rating):
        self.rating = rating
        db.session.commit()

    # Delete deletes a user's rating from databse. 
    def Delete(self):
        db.session.delete(self)
        db.session.commit()
        
# -------------------    Reviews  ----------------------# #----3----#

class Reviews(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)

    def __str__(self):
        return f"user with id ({self.user_id}) reviewed [{self.review}] for book with id ({self.book_id})"

    # EditReview edits a user's review.
    def EditReview(self, review):
        self.review = review
        db.session.commit()

    # Delete deletes a user's review from databse.
    def Delete(self):
        db.session.delete(self)
        db.session.commit()


# -------------------    Orders  ----------------------# #----4----#

class Orders(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    order_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean, default = False, nullable=False)

    def __str__(self):
        return f"user with id ({self.user_id}) ordered for book with id ({self.book_id}) in {self.order_time} "

    #Deliver sets order statue to True to indicate it is delivered.
    def Deliver(self):     
        self.status= True
        db.session.commit()

    #Delete deletes an order from database and calls Return_Copy method. It rasies an exception of the order is already deliverd.
    def Delete(self):
        if not self.status:
            book = Books.query.get(self.book_id)
            book.Return_Copy()
            db.session.delete(self)
            db.session.commit()            
        else:
            raise Exception('Unable to delete order. Book Already Delivered.')


# -------------------    Author  ----------------------# #----5----#
class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key =  True)
    name = db.Column(db.String, unique = True)
    birth = db.Column(db.DateTime, nullable=True)
    death= db.Column(db.DateTime, nullable=True)
    bio = db.Column(db.String, nullable=True)

    def __str__(self):
        return f"{self.name}"

# -------------------    Actor  ----------------------# #----6----#
'''
- Actor Abstract object:
  attrs:
    email (received it verified. It will be a string)
    password (recieved it hashed. It will be of Bytes type)
    name
    permissions (False by default)
  Actor has no methods
  User and Admin inherit from Actor
'''
class Actor(db.Model):
    __tablename__ = "actors"
    __mapper_args__ = {'polymorphic_identity': 'actors'}

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique = True, nullable=False)
    password = db.Column(db.String, unique = True, nullable=False)
    name = db.Column(db.String, unique = True, nullable=False)
    permissions= db.Column(db.Boolean, default = False, nullable=False)



    def __str__(self):
        return f"{self.name}"

# -------------------   Actor > User  ----------------------# #----7----#
class User(Actor):
    __tablename__ = "users"
    __mapper_args__ = {'polymorphic_identity': 'users'}

    id = db.Column(db.Integer, db.ForeignKey('actors.id'), primary_key=True)
    birth = db.Column(db.DateTime, nullable=True)
    visa= db.Column(db.Integer, nullable=False)
    address = db.Column(db.String, unique = True, nullable=False)


# -------------------   Actor > Admin  ----------------------# #----8----#
class Admin(Actor):
    __tablename__ = "admins"
    id = db.Column(db.Integer, db.ForeignKey('actors.id'), primary_key=True)

    # set permissions to True for Admin objects when created to set them aside from User objects.
    def __init__(self, **kwargs):
        super(Admin, self).__init__(**kwargs)
        self.permissions = True

