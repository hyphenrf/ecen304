class Book:
    def __init__(self,isbn,title,author,year,stock,sold,borrowed,price):
        #TODO: do we need to put some of those non-identifying optional info in a dict?
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year #TODO: Maybe make this int and do checks on it? `not year > current_year`?
        self.stock = int(stock)
        self.sold = int(sold)
        self.borrowed = int(sold)
        self.available= int(stock)-int(sold)-int(borrowed)
        self.price = float(price)
        self.ratings = {} #TODO: Dicts {userID: float(rating)}
        self.reviews = {}
    
    def EditBook_Basic(self,isbn,title,author,year,price):
        #TODO: change this to working with dicts to allow data flexibility
        # SEE ALSO: backend/actor.py: edit_info()
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.price = price
    
    def EditBook_Num(self,stock,sold,borrowed):
        #TODO: borrow, buy, return
        self.stock = stock
        self.sold = sold
        self.borrowed = borrowed
        self.available= stock-sold-borrowed

    def rate(self,user, rating):
        return {user: rating}

    def review(self,user, review):
        return {user: review}

