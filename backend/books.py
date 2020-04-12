
import csv
import random 

Books=[]
class Book:
    def __init__(self,isbn,title,author,year,total,sold,borrowed,available,price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.total = total
        self.sold = sold
        self.borrowed = borrowed
        self.available= available
        self.price = price
        self.ratings = []
        self.reviews = []
    
    def EditBook_Basic(self,isbn,title,author,year,price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.price = price
    
    def EditBook_Num(self,total,sold,borrowed,available):
        self.total = total
        self.sold = sold
        self.borrowed = borrowed
        self.available = available

    def Rating(self,user, rating):
        new = {"User": user, "Rating": rating}
        self.ratings.append(new)

    def Review(self,user, review):
        new = {"User": user, "Review": review}
        self.review.append(new)    
        


def main():
    # load books.csv
    f=open("books.csv")
    reader =csv.reader(f)
    #create book objects
    for isbn,title,author,year in reader:

        price = round(random.uniform(50,400),2)
        total = random.randrange(100, 501, 1)
        sold = random.randrange(0, 501, 1)
        borrowed = random.randrange(0, 501, 1)
        available = random.randrange(0, 501, 1)

        while total != sold + borrowed + available:
            sold = random.randrange(0, 501, 1)
            borrowed = random.randrange(0, 501, 1)
            available = random.randrange(0, 501, 1)  
        
        if year != "year":        
            book=Book(isbn,title,author,year,total,sold,borrowed,available,price)            
            #list of book objects
            Books.append(book)
    
    # show list of Books
    for book in Books:
        print ('ISBN: %s - Title: %s - Author: %s - Year: %s - Total: %d - Sold: %d - Borrowed: %d - Available: %d - Price: %f' % (book.isbn,book.title,book.author,book.year,book.total,book.sold,book.borrowed,book.available,book.price))
        
    print("done")            
    


if __name__ == "__main__":
    main()