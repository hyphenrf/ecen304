import threading
from datetime import datetime
from datetime import timedelta
from modelsBooks import *
from modelsBooks import EditBook_Num


today = datetime.now()

# Mehtaga el code dah yeb2a sql at2ked kol youm

def UpdateOrders():
  #threading.Timer(86400, UpdateOrders).start()
  threading.Timer(86400, UpdateOrders).start()

  orders = Orders.query.all()
  for order in orders:
      # today >= (to consider difference in hours and minutes)
        #if today >= order.order_time + timedelta(days = 3):
        if today >= order.order_time + timedelta(seconds = 3):
          
          order.status = True
          book_ordered_row = Books.query.get(order.book_id)
          book_ordered_row.sold += 1
          EditBook_Num(order.book_id, book_ordered_row.total,book_ordered_row.sold)

  db.session.commit()        
  


      

