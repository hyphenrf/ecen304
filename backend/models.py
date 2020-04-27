import csv
import os
import random 
from datetime import datetime
from datetime import timedelta
import threading

Books=[]
BendingOrders=[]
DeliveredOrders=[]
BorrowedBooks = []
LateBooks=[]

today = datetime.now()


def UpdateOrders():
  threading.Timer(5, UpdateOrders).start()

  for order in BendingOrders:
      # today >= (to consider difference in hours and minutes)
      if today >= order["Time"] + timedelta(3):
          #change state of book to "delivered" before appending to DeliveredOrders 
          order["State"] = "Delivered"
          DeliveredOrders.append(order)
          BendingOrders.remove(order)

  for book in BorrowedBooks:
       
      if today >= book["Return time"]:
        #change state of book to "late" before appending to LateBooks
        book["State"] = "Late"
        LateBooks.append(book)
        BorrowedBooks.remove(book)


UpdateOrders()

class Book:
    def __init__(self,isbn,title,author,year,total,sold,borrowed,price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.total = total
        self.sold = sold
        self.borrowed = sold
        self.available= total-sold-borrowed
        self.price = price
        self.ratings = []
        self.reviews = []
    
    def EditBook_Basic(self,isbn,title,author,year,price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.price = price
    
    def EditBook_Num(self,total,sold,borrowed):
        self.total = total
        self.sold = sold
        self.borrowed = borrowed
        self.available= total-sold-borrowed

    def OrderBook(self,user):
        order = {"User": user, "Book": self, "Time": today, "State":"To be delivered within three days."}
        BendingOrders.append(order)
        self.total -= 1
        self.available -= 1
        self.sold += 1

    def BorrowBook(self, user, days):
        return_day = today + timedelta(days)
        borrow = {"User": user, "Book": self, "Borrow time": today, "Return time": return_day, "State":"Borrowerd. To be Returned."}
        BorrowedBooks.append(borrow)
        self.total -= 1
        self.available -= 1
        self.borrowed += 1

   #returned books don't have a list. The are just removed from BorrowedBooks or LateBooks and total is increased.          
    def ReturnBook(self, user):
        for borrow_dict in BorrowedBooks:
            if borrow_dict["User"] == user and borrow_dict["Book"] == self :
                self.total += 1
                self.available += 1
                self.borrowed -= 1
                BorrowedBooks.remove(borrow_dict)        
            else:
                for late_dict in LateBooks:
                    if late_dict["User"] == user and late_dict["Book"] == self :
                        self.total += 1
                        self.available += 1
                        self.borrowed -= 1
                        LateBooks.remove(late_dict)



    def RateBook(self,user, rating):
        new = {"User": user, "Rating": rating}
        self.ratings.append(new)

    def ReviewBook(self,user, review):
        new = {"User": user, "Review": review}
        self.reviews.append(new)    
        


def main():
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
    main()