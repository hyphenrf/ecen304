#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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


#def OrderBook(self,user,isbn):
#    #TODO: This is a DB function
#    for book in books:
#        if book.isbn == isbn:
#            time = datetime.now()
#            order = {
#                    "User": user, 
#                    "Book": book, 
#                    "time": time, 
#                    "state":"To be delivered within three days."
#                    }
#            BendingOrders.append(order)
#            self.total -= 1
#            self.sold += 1



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
