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

    f=open(os.path.abspath("backend/books.csv"),'r')
    reader =csv.reader(f)
    for isbn,title,author,year,total,sold,price in reader:        
        count=  Author.query.filter_by(name=author).count()
        if count == 0:
            #create Author objects
            author_obj= Author(name= author)
            db.session.add(author_obj) 
        db.session.commit()

        author_query= Author.query.filter_by(name=author).first() 
        #create book objects
        book = Books(isbn = isbn,title = title, author = author, author_id = author_query.id, year = int(year),total = int(total),sold = int(sold), price = float(price))
        db.session.add(book)
        #commit changes to database
        db.session.commit()    
    
   
if __name__ == "__main__":
    with app.app_context():
        main()


