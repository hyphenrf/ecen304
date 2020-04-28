import csv
import os

from flask import Flask, render_template, request
from models_ex import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://nynvjnzdwddjcx:09d28298ab43f17d54fb573194bdde2962a0b08f823369f98c014a0df1bc94c4@ec2-34-202-7-83.compute-1.amazonaws.com:5432/dabb7iss8h6876"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.session.commit()

# Dah nezbto shabh ely fo2

    # load books.csv
    #f-open("Updated_books.csv")
    f=open(os.path.abspath("Updated_books.csv"),'r')
    reader =csv.reader(f)
    #create book objects
    for isbn,title,author,year,total,sold,borrowed,price in reader:
       
        book=Book(isbn,title,author,int(year),int(total),int(sold),int(borrowed),float(price))            
        #list of book objects
        Books.append(book)  

if __name__ == "__main__":
    with app.app_context():
        main()
