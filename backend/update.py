import threading
from datetime import datetime
from datetime import timedelta
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
  threading.Timer(86400, UpdateOrders).start()
  today = datetime.now()
 
  orders = Orders.query.all()
  for order in orders:
    if today >= order.order_time + timedelta(days = 3):
      #for testing
    #if today >= order.order_time + timedelta(seconds = 3): 
        order.Deliver()
          


    
if __name__ == "__main__":
    with app.app_context():
        main()



      

