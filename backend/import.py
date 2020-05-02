import csv
import os


from flask import Flask, render_template, request
from modelsBooks import *
from modelsBooks import EditBook_Basic, OrderBook, RateBook, ReviewBook
from update import *

app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://ayasafan:25399@localhost/books"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://salmazakzouk:abcd1234@localhost/Books"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():

    # Run only for the first time to fill the tables

    

    # load books.csv
    #f-open("Updated_books2.csv")
    f=open(os.path.abspath("Updated_books2.csv"),'r')
    reader =csv.reader(f)
    #create book objects
    for isbn,title,author,year,total,sold,price in reader:
        book = Books(isbn = isbn,title = title,author = author,year = int(year),total = int(total),sold = int(sold), available = int(int(total) - int(sold)), price = float(price)) 
        db.session.add(book)   
    db.session.commit()

    # load Users_info.csv
    f=open(os.path.abspath("Users_info.csv"),'r')
    reader =csv.reader(f)
    #create book objects
    for name in reader:
        user = Users(user_name = name) 
        db.session.add(user) 
    # There is a problem in reading the first name correctly from file
    delete_user1 = Users.query.get(1)
    db.session.delete(delete_user1)

    db.session.commit()


    

    # Working

    #EditBook_Basic(2, 300)
    #OrderBook(2, 2)
    #RateBook(2, 5, 2)
    #ReviewBook(2, "Fantastic!", 2)
    #UpdateOrders()



 

if __name__ == "__main__":
    with app.app_context():
        main()


