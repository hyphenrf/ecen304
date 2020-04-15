from .util import _verify_date, _hashed, _verify_email


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
        EditAddress()

        #REMOVING
        deleteShelf() later on
        removeUser()
    '''

    def __init__(self, email, pwd, name='Jay', dob=None):
        self.name = name
        self.dob = _verify_date(dob)
        self.email = _verify_email(email)
        self.pwd = _hashed(pwd)
        self.visaSerial = ''
        self.borrowed = []
        self.bought = []
        self.pending = []
        self.rated = {}
        self.comments = {}
        self.address = {}

    def addRating(self, bookID: int, rate: int):
        self.rated[bookID] = rate
        return self.rated

    def addComment(self, bookID: int, comment: str):
        self.rated[bookID] = comment
        return self.comments

    def VisaSerial(self, visaSerial: int):
        if len(visaSerial) < 12:
            raise Exception('Invalid VISA serial number')
        else:
            self.visaSerial = visaSerial
        return self.visaSerial

    def borrow(self, bookID: int):
        self.borrowed.append(bookID)
        return self.borrowed

    def buy(self, bookID: int):
        self.bought.append(bookID)
        return self.bought

    def addAddress(self, lat: float, long: float, addressName):
        self.address[addressName] = {lat, long}
        return self.address

    def editName(self, data):
        self.name = data
        return self.name

    def editDob(self, data):
        self.dob = data
        return self.dob

    def editPwd(self, data):
        self.pwd = _hashed(data)

    def editEmail(self, data):
        self.name = _verify_email(data)
        return self.email

    def removeUser(self, id):
        return None
