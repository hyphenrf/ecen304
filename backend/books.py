import csv
#import os
import random 
from datetime import datetime
import threading

Books=[]
BendingOrders=[]
Delivered=[]

def UpdateOrders():
  threading.Timer(86400, UpdateOrders).start()
  ''' ckeck date to see if 3 days passed for each dictionary in BendingOrders.
  If yes: Update state and remove from BendingOrders and add to Delivered.
  '''
UpdateOrders()

class Book:
    def __init__(self,isbn,title,author,year,total,sold,borrowed,price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.total = int(total)
        self.sold = int(sold)
        self.borrowed = int(sold)
        self.available= int(total)-int(sold)-int(borrowed)
        self.price = float(price)
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

    def OrderBook(self,user,isbn):
        for book in books:
            if book.isbn == isbn:
                time = datetime.now()
                order = {"User": user, "Book": book, "time": time, "state":"To be delivered within three days."}
                BendingOrders.append(order)
                self.total -= 1
                self.sold += 1

    def RateBook(self,user, rating):
        new = {"User": user, "Rating": rating}
        self.ratings.append(new)

    def ReviewBook(self,user, review):
        new = {"User": user, "Review": review}
        self.review.append(new)    
        


def main():
    # load books.csv
    #os.chdir(r'C:\Users\ascom\Downloads\Documents\304 software\git\ecen304\backend')
    f=open("Updated_books.csv")
    reader =csv.reader(f)
    #create book objects
    for isbn,title,author,year,total,sold,borrowed,price in reader:
       
        book=Book(isbn,title,author,year,total,sold,borrowed,price)            
        #list of book objects
        Books.append(book)
    
    # show list of Books
    for book in Books:
        print ('ISBN: %s , Title: %s , Author: %s , Year: %s , Total: %d , Sold: %d , Borrowed: %d , Available: %d , Price: %d' % (book.isbn,book.title,book.author,book.year,book.total,book.sold,book.borrowed,book.available,book.price))
        
    print("done")            
    

if __name__ == "__main__":
    main()