import threading
from datetime import datetime
from datetime import timedelta
from modelsBooks import *


today = datetime.now()

# Mehtaga el code dah yeb2a sql at2ked kol youm

def UpdateOrders():
  threading.Timer(86400, UpdateOrders).start()

  orders = Orders.query.all()
  for order in orders:
      # today >= (to consider difference in hours and minutes)
      if today >= order.order_time + timedelta(days = 3):
          order.status = True
      

