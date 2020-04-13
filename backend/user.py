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
        Payment method: <<<UNSURE>>> 
        Savings in account 
        Address: String/Pair<Float, Float> ← coordinates?


    Methods:
        #ADDING => adding the author is done when the class instance is initiated
        addShelf() later on
        addBookToShelf() later on

        #EDITING
        editName()
        editDob()
        editPwd()
        editEmail()

        #REMOVING
        deleteShelf() later on
        removeUser()
    '''

    def __init__(self, email, pwd, name='Jay', dob=None):
        self.name = name
        self.dob = dateValidator(dob)
        self.email = _verify_email(email)
        self.pwd = _hashed(pwd)
        self.lob = []

    def addGenre(self, data):
        if(isinstance(data, str)):
            self.genre.append(data)
        else:
            print('Data not a string')

    def editGenre(self, equal, change):
        for i in range(len(self.genre)):
            if self.genre[i] == equal:
                self.genre[i] = change
        return self.genre

    def removeGenre(self, data):
        filter(lambda genre: genre == data, self.genre)
        return self.genre

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

    def removeAuthor(self, id):
        return None
