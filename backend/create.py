import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://nynvjnzdwddjcx:09d28298ab43f17d54fb573194bdde2962a0b08f823369f98c014a0df1bc94c4@ec2-34-202-7-83.compute-1.amazonaws.com:5432/dabb7iss8h6876"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
