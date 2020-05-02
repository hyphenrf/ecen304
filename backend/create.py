
import os


from flask import Flask, render_template, request
from modelsBooks import *

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://ayasafan:25399@localhost/books"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://salmazakzouk:abcd1234@localhost/Books"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
