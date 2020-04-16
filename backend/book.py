'''module docstring here'''



class Book:
    '''Insert your documentation here
    notes on some of this class properties:
    - id is synonym to isbn
    - borrow_limit is int of days
    - warranty is int of days
    - A book is considered pending until n warranty days after its arrival
    - properties that shouldn't be modified by-hand were made read-only
      Those are:
      - id
      - available, borrowed, pending, sold, stock
      - ratings, reviews, ratings_avg
    - The rest are free to directly modify, just be mindful of data
      correctness.


    methods in this class may raise ValueError 
    depending on the values available at runtime.
    '''
    # note: attrs declared here retain value after re-initialization,
    #       but reset on a new object initialization. (objs are mutable).

    # note: these three values maintain a strong logical relationship, so they
    #       were privated aggressively.
    ##############
    __borrowed = 0
    __pending = 0
    __stock = 1
    ##############

    _sold = 0
    _ratings = {}
    _reviews = {}

    def __init__(self, isbn: int, title: str, author_ids: [int], year: int,
            edition: int = 1):
        # These define a unique object
        self.isbn = isbn
        self.title = title
        self.author = author_ids
        self.year = year
        self.edition = edition

        # These don't
        self.is_borrow = False
        self.borrow_limit = 7
        self.is_sell = False
        self.warranty = 0
        self.price = 0.0

    @property
    def id(self): return self.isbn
    @property # read-only
    def available(self): 
        return self.__stock - (self.__borrowed + self.__pending)

    @property
    def borrowed(self): return self.__borrowed

    @property
    def pending(self): return self.__pending

    @property
    def sold(self): return self._sold

    @property
    def ratings(self): return self._ratings

    @property
    def reviews(self): return self._reviews

    @property
    def ratings_avg(self):
        if ratings:
            l = len(ratings)
            return sum(ratings.values())/l, l
        else:
            return 0, 0

    def change_stock(self, diff: int) -> None:
        n = self.__stock + diff
        if n > (self.__borrowed + self.__pending):
            self.__stock = n
        else:
            raise ValueError("You can't have negative stock.")

    def rate(self, user: int, rating: float) -> None:
        self._ratings[user] = rating

    def review(self, user: int, review: str) -> None:
        self._reviews[user] = review

    def order(self, num: int = 1) -> None:
        if self.is_sell and num <= self.available:
            self.__pending += num
        else:
            raise ValueError("can't buy this much or unsellable book.")

    def order_sold(self, num: int = 1) -> None:
        if num <= self.__pending:
            self.__pending -= num
            self.__stock -= num
            self._sold += num
        else:
            raise ValueError("selling more than there is pending.")

    def order_return(self, num: int = 1) -> None:
        if num <= self.__pending:
            self.__pending -= num
        else:
            raise ValueError("returning more than there is pending.")

    def borrow(self, num: int = 1) -> None:
        if self.is_borrow and num <= self.available:
            self.__borrowed += num
        else:
            raise ValueError("can't borrow this much or unborrowable book.")

    def borrow_return(self, num: int = 1) -> None:
        if num <= self.__borrowed:
            self.__borrowed -= num
        else:
            raise ValueError("returning more than there is borrowed.")

