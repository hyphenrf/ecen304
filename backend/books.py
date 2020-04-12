
import csv

Books=[]
class Book:

    no_of_avilable_books = 200
    no_of_borrowed = 0
    no_of_sold = 0

    def __init__(self,isbn,title,author,year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

   

def main():
    
    f=open("books.csv")
    reader =csv.reader(f)
    for isbn,title,author,year in reader:
        if year != "year":        
            book=Book(isbn,title,author,year)
            Books.append(book)
    
    for book in Books:
        print ('ISBN: %s - Title: %s - Author: %s - Year: %s' % (book.isbn,book.title,book.author,book.year))
        
    print("done")            
    


if __name__ == "__main__":
    main()