from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Books(db.Model):
    __tablename__ = "books"
    # dawary 3ala unique (Lazem) -- > Done
    id = db.Column(db.Integer, primary_key =  True)
    isbn = db.Column(db.Integer, unique = True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    # maximum value 2020 --> Done
    year = db.Column(db.Integer, db.CheckConstraint('year <= 2020') ,nullable=False)
    total = db.Column(db.Integer, nullable=False)
    # mehtaga adwar 3ala default 0 --> Done
    sold = db.Column(db.Integer, default = 0 ,nullable=False)
    price = db.Column(db.Double, nullable=False)



class Ratings(db.Model):
    __tablename__ = "ratings"
    id = db.Column(db.Integer, primary_key=True)
    # constrain 0 le 5 --> Done
    rating = db.Column(db.Integer, db.CheckConstraint('0 <= rating <= 5') ,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)

# Na2es yetkmel --> Done
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)

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


