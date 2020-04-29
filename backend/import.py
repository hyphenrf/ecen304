import csv
import os

from flask import Flask, render_template, request
from modelsBooks import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://nynvjnzdwddjcx:09d28298ab43f17d54fb573194bdde2962a0b08f823369f98c014a0df1bc94c4@ec2-34-202-7-83.compute-1.amazonaws.com:5432/dabb7iss8h6876"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():

    # load books.csv
    #f-open("Updated_books2.csv")
    f=open(os.path.abspath("Updated_books2.csv"),'r')
    reader =csv.reader(f)
    #create book objects
    for isbn,title,author,year,total,sold,price in reader:
        book = Books(isbn = isbn,title = title,author = author,year = int(year),total = int(total),sold = int(sold),price = float(price))   
        db.session.add(book)   
    db.session.commit()
 

if __name__ == "__main__":
    with app.app_context():
        main()
