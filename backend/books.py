import csv
import os
from datetime import datetime
import threading

#TODO: This is DB/State functionality, A class is concerned only with a single book.
#Books=[]
#BendingOrders=[]
#Delivered=[]

#def UpdateOrders():
#  ''' ckeck date to see if 3 days passed for each dictionary in BendingOrders.
#  If yes: Update state and remove from BendingOrders and add to Delivered.
#  '''
#  threading.Timer(86400, UpdateOrders).start()
#UpdateOrders()

class Book:
    def __init__(self,isbn,title,author,year,total,sold,borrowed,price):
        #TODO: do we need to put some of those non-identifying optional info in a dict?
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year #TODO: Maybe make this int and do checks on it?
        self.stock = int(stock)
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
                order = {
                        "User": user, 
                        "Book": book, 
                        "time": time, 
                        "state":"To be delivered within three days."
                        }
                BendingOrders.append(order)
                self.total -= 1
                self.sold += 1

    def RateBook(self,user, rating):
        new = {"User": user, "Rating": rating}
        self.ratings.append(new)

    def ReviewBook(self,user, review):
        new = {"User": user, "Review": review}
        self.review.append(new)    
        


#def main():
#    # load books.csv
#    #f-open("Updated_books.csv")
#    f=open(os.path.abspath("backend\\Updated_books.csv"),'r')
#    reader =csv.reader(f)
#    #create book objects
#    for isbn,title,author,year,total,sold,borrowed,price in reader:
       
#        book=Book(isbn,title,author,year,total,sold,borrowed,price)            
#        #list of book objects
#        Books.append(book)
    
#    # show list of Books
#    for book in Books:
#        print ('ISBN: %s , Title: %s , Author: %s , Year: %s , Total: %d ,'
#        ' Sold: %d , Borrowed: %d , Available: %d , Price: %d' 
#        % (book.isbn,book.title,book.author,book.year,book.total,book.sold,
#        book.borrowed,book.available,book.price))
        
#    print("done")            
    

#if __name__ == "__main__":
#    main()
