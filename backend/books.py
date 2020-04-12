
import csv

Books=[]
class Book:
    def __init__(self,isbn,title,author,year,total,sold,borrowed):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.total = total
        self.sold = sold
        self.borrowed = borrowed
    
    def EditBook_Basic(self,isbn,title,author,year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
    
    def EditBook_Num(self,total,sold,borrowed):
        self.total = total
        self.sold = sold
        self.borrowed = borrowed
        
        


def main():
    # load books.csv
    f=open("books.csv")
    reader =csv.reader(f)
    #create book objects
    for isbn,title,author,year in reader:
        if year != "year":        
            book=Book(isbn,title,author,year)
            #list of book objects
            Books.append(book)
    
    # show list of Books
    for book in Books:
        print ('ISBN: %s - Title: %s - Author: %s - Year: %s' % (book.isbn,book.title,book.author,book.year))
        
    print("done")            
    


if __name__ == "__main__":
    main()p