import csv
import os


from flask import Flask, render_template, request
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://ayasafan:25399@localhost/books"
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://salmazakzouk:abcd1234@localhost/Books"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():

    # test add user
    '''
    user = Users(user_name="Aya Safan")
    db.session.add(user)    
    db.session.commit()
    '''

    # test EditBook_Num 
    '''
    book = Books.query.get(3)
    print(book)
    book.EditBook_Num(250,200)
    print(book)
    '''
    # test OrderBook 
    '''
    book = Books.query.get(5)
    book.OrderBook(2)
    order = Orders.query.get(1)
    print(order)
    '''
    # test RateBook 
    '''
    book = Books.query.get(2)
    book.RateBook(1,4)
    rating = Ratings.query.get(1)
    print(rating)
    
    '''
    # test EditRate 
    '''
    book = Books.query.get(2)
    book.EditRate(1,3)
    rating = Ratings.query.get(1)
    print(rating)
    '''

    # text Orders Delete
    '''
    order = Orders.query.get(5)
    order.Delete()

    '''   

    
if __name__ == "__main__":
    with app.app_context():
        main()


