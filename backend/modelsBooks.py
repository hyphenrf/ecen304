from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from datetime import timedelta

db = SQLAlchemy()
today = datetime.now()

# -------------------    Tables to be created  ----------------------#

class Books(db.Model):
    __tablename__ = "books"
    # dawary 3ala unique (Lazem) -- > Done
    id = db.Column(db.Integer, primary_key =  True)
    isbn = db.Column(db.String, unique = True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    # maximum value 2020 --> Done
    year = db.Column(db.Integer, db.CheckConstraint('year <= 2020') ,nullable=False)
    total = db.Column(db.Integer, nullable=False)
    # mehtaga adwar 3ala default 0 --> Done
    sold = db.Column(db.Integer, default = 0 ,nullable=False)
    available = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Na2es yetkmel --> Done
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)

class Ratings(db.Model):
    __tablename__ = "ratings"
    id = db.Column(db.Integer, primary_key=True)
    # constrain 0 le 5 --> Done
    rating = db.Column(db.Integer, db.CheckConstraint('0 <= rating AND rating <= 5') ,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)


class Orders(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    # Dawry 3ala type el date --> Done
    order_time = db.Column(db.DateTime, nullable=False)
    # Zabaty dah...el default beta3o mawslsh (True we false) --> Done
    status = db.Column(db.Boolean, default = False, nullable=False)


class Reviews(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)


# ---------------------------   Methods for updating database --------------------#

def EditBook_Num(book_id, total,sold):

    
    book = Books.query.get(book_id)
    book.total = total
    book.sold = sold
    book.available = total-sold
    db.session.commit()
    


def EditBook_Basic(book_id, price):

    book = Books.query.get(book_id)
    book.price = price
    db.session.commit()


def OrderBook(user_id,book_id):
    
    order = Books.query.get(book_id)
    if book_id == order.id:
        new_order = Orders(user_id = user_id, book_id = order.id, order_time = today, status = False)
        db.session.add(new_order)
    db.session.commit()

def RateBook(user_id, rating, book_id):
    rated_book_row = Books.query.get(book_id)
    rating = Ratings(rating = rating, user_id = user_id, book_id = rated_book_row.id)
    db.session.add(rating)
    db.session.commit()

def ReviewBook(user_id, review, book_id):
    reviewed_book_row = rated_book_row = Books.query.get(book_id)
    review = Reviews(review = review, user_id = user_id, book_id = reviewed_book_row.id)
    db.session.add(review)
    db.session.commit()

