from .util import _hashed, _salt
from .book import Book



class User:
    '''Author class is resposnible for the Authos's data managment
    Atribs:
        id: int
        email: str
        passwd: str
        name: str
        dob (date of birth): tuple

        address: tuple(str, tuple(float, float))
        visa_serial: int

    Relating to the Book class:
        borrowed: set(Book.id)
        pending: { Book.id: int(amount) }
        bought: { Book.id: int(amount) }
        ratings: { Book.id : int(rating1-5) }
        comments: { Book.id : str(comment) }


    Methods:
        #ADDING => adding the author is done when the class instance is initiated
        addShelf() later on
        addBookToShelf() later on
        addRating()
        addComment()
        addVisaSerial() => adds, edits and checks for validity
        borrow()
        buy()
        addAddress() 

        #EDITING
        editName()
        editDob()
        editPwd()
        editEmail()
        editRating()
        editComment()
        editAddress()

        #REMOVING
        deleteShelf() later on
        removeUser()
        removeRating()
        removeComment()
        removeAddress()
    '''

    def __init__(self, email: str, pwd: str, name='Jay', dob=None):

        #ASSERTIONS
        assert isinstance(pwd, str), "Password must be a string"
        assert isinstance(email, str), "Email must be a string"
        assert isinstance(name, str), "Name must be a string"

        self.name = name
        self.dob = dob
        self.email = email
        self.pwd = _hashed(pwd)
        self.visaSerial = 0
        self.borrowed = {}
        self.bought = {}
        self.pending = {}
        self.rated = {}
        self.comments = {}
        self.address = {}

    # ADDING

    def add_rating(self, bookID: int, rate: int) -> dict:
        self.rated[bookID] = rate
        return self.rated

    def add_comment(self, bookID: int, comment: str) -> dict:
        self.rated[bookID] = comment
        return self.comments

    def visa_serial(self, visaSerial: int) -> int:
        if len(visaSerial) < 12:
            raise Exception('Invalid VISA serial number')
        else:
            self.visaSerial = visaSerial
        return self.visaSerial

    def borrow(self, bookID: int) -> list:
        self.borrowed.append(bookID)
        return self.borrowed

    def buy(self, bookID: int) -> list:
        self.bought.append(bookID)
        return self.bought

    def add_address(self, lat: float, long: float, addressName: str) -> dict:
        self.address[addressName] = {lat, long}
        return self.address

    # EDITING
    def edit_name(self, data: str) -> str:
        self.name = data
        return self.name

    def edit_dob(self, data: str) -> str:
        self.dob = data
        return self.dob

    def edit_pwd(self, data):
        self.pwd = _hashed(data)

    def edit_email(self, data: str) -> str:
        self.name = data
        return self.email

    def edit_rating(self, bookID: int, rate: int) -> dict:
        if self.rated[bookID]:
            self.rated[bookID] = rate
        else:
            raise Exception('Book not found. Please enter a valid ID')
        return self.rated

    def edit_comment(self, bookID: int, comment: str) -> dict:
        if self.comments[bookID]:
            self.comments[bookID] = comment
        else:
            raise Exception('Book not found. Please enter a valid ID')
        return self.comments

    def edit_address(self, lat: float, long: float, addressName: str) -> dict:
        if self.address[addressName]:
            self.address[addressName] = {lat, long}
        else:
            raise Exception(
                'Address Name not found. Please enter a valid Address Name')
        return self.address

    # REMOVING

    def remove_rating(self, bookID: int) -> dict:
        if self.rated[bookID]:
            self.rated.pop(bookID)
        else:
            raise Exception('Book not found. Please enter a valid ID')
        return self.rated

    def remove_comment(self, bookID: int) -> dict:
        if self.comments[bookID]:
            self.comments.pop(bookID)
        else:
            raise Exception('Book not found. Please enter a valid ID')
        return self.comments

    def remove_address(self, addressName: str) -> dict:
        if self.address[addressName]:
            self.address.pop(addressName)
        else:
            raise Exception('Book not found. Please enter a valid ID')
        return self.address
