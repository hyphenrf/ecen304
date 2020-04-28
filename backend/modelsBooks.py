from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Books(db.Model):
    __tablename__ = "books"
    # dawary 3ala unique (Lazem)
    isbn = db.Column(db.Integer, Unique = True)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    dauthor = db.Column(db.String, nullable=False)
    # maximum value 2020 
    year = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    ''' mehtaga adwar 3ala default 0 '''
    sold = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Double, nullable=False)



class Ratings(db.Model):
    __tablename__ = "ratings"
    id = db.Column(db.Integer, primary_key=True)
    # constrain 0 le 5
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)

# Na2es yetkmel
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)

class Orders(db.Model):
    __tablename__ = "orders"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    # Dawry 3ala type el date
    time = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    # Zabaty dah...el default beta3o mawslsh (True we false)
    status = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)


class Reviews(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    # constrain 0 le 5
    review = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)


