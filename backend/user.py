from .util import dateValidator, _hashed, _verify_email


class User:
    '''Author class is resposnible for the Authos's data modification and managment
    Atribs:
        ID: Int
        Name: String
        Date of birth (dob): Int:EPOCH
        List of books (lob): List<Int:ID>
        Email: str
        Password (pwd): str
        Borrowed books: List<Int:ID>
        Bought books: List<Int:ID>
        Pending books: List<Int:ID>
        Rated books => ratings Dict:{Int:ID-Book : Int:Rating1-5}
        comments=> comments Dict:{Int:ID-Book : str:comment}
        Address: object Dict:{lat:float, long:float} ← coordinates?

        Payment method: <<<UNSURE>>> 
        Savings in account 


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

    def __init__(self, email, pwd, name='Jay', dob=None):
        self.name = name
        self.dob = dateValidator(dob)
        self.email = _verify_email(email)
        self.pwd = _hashed(pwd)
        self.visaSerial = 0
        self.borrowed = []
        self.bought = []
        self.pending = []
        self.rated = {}
        self.comments = {}
        self.address = {}

    # ADDING

    def addRating(self, bookID: int, rate: int) -> dict:
        self.rated[bookID] = rate
        return self.rated

    def addComment(self, bookID: int, comment: str) -> dict:
        self.rated[bookID] = comment
        return self.comments

    def VisaSerial(self, visaSerial: int) -> int:
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

    def addAddress(self, lat: float, long: float, addressName: str) -> dict:
        self.address[addressName] = {lat, long}
        return self.address

    # EDITING
    def editName(self, data: str) -> str:
        self.name = data
        return self.name

    def editDob(self, data: str) -> str:
        self.dob = data
        return self.dob

    def editPwd(self, data):
        self.pwd = _hashed(data)

    def editEmail(self, data: str) -> str:
        self.name = _verify_email(data)
        return self.email

    def editRating(self, bookID: int, rate: int) -> dict:
        if self.rated[bookID]:
            self.rated[bookID] = rate
        else:
            raise Exception('Book not found. Please enter a valid ID')
        return self.rated

    def editComment(self, bookID: int, comment: str) -> dict:
        if self.comments[bookID]:
            self.comments[bookID] = comment
        else:
            raise Exception('Book not found. Please enter a valid ID')
        return self.comments

    def editAddress(self, lat: float, long: float, addressName: str) -> dict:
        if self.address[addressName]:
            self.address[addressName] = {lat, long}
        else:
            raise Exception(
                'Address Name not found. Please enter a valid Address Name')
        return self.address

    # REMOVING
    def removeUser(self, id):
        return None

    def removeRating(self, bookID: int) -> dict:
        if self.rated[bookID]:
            self.rated.pop(bookID)
        else:
            raise Exception('Book not found. Please enter a valid ID')
        return self.rated

    def removeComment(self, bookID: int) -> dict:
        if self.comments[bookID]:
            self.comments.pop(bookID)
        else:
            raise Exception('Book not found. Please enter a valid ID')
        return self.comments

    def removeAddress(self, addressName: str) -> dict:
        if self.address[bookID]:
            self.address.pop(addressName)
        else:
            raise Exception('Book not found. Please enter a valid ID')
        return self.address
