import threading
from datetime import datetime
from datetime import timedelta
from modelsBooks import *


today = datetime.now()

# Mehtaga el cod dah yeb2a sql at2ked kol youm

def UpdateOrders():
  threading.Timer(5, UpdateOrders).start()

  for order in BendingOrders:
      # today >= (to consider difference in hours and minutes)
      if today >= order["Time"] + timedelta(3):
          #change state of book to "delivered" before appending to DeliveredOrders 
          order["State"] = "Delivered"
          DeliveredOrders.append(order)
          BendingOrders.remove(order)