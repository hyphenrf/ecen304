from email_validator import validate_email, EmailNotValidError
from passlib.hash import pbkdf2_sha256
from util import dateValidator


class Author:
    '''Author class is resposnible for the Authos's data modification and managment
    Atribs:
        ID: Int
        Name: String
        Date of birth (dob): Int:EPOCH
        List of books (lob): List<Int:ID>
        Genres: List<String>
        Email: str
        Password (pwd): str

    Methods:
        #ADDING => adding the author is done when the class instance is initiated
        addGenre()
        addBook()

        #EDITING
        editGenre()
        editBook()
        editName()
        editDob()
        editPwd()
        editEmail()

        #REMOVING
        removeGenre()
        removeBook()
        removeAuthor()
    '''

    def __init__(self, email, pwd, name='Jay', dob=None):
        self.name = name
        self.genre = []
        self.lob = []
        self.dob = dateValidator(dob)
        self.email = validate_email(email)
        self.pwd = pbkdf2_sha256.hash(pwd)

    def addGenre(self, data):
        if(isinstance(data, str)):
            self.genre.append(data)
        else:
            print('Data not a string')

    def editGenre(self, equal, change):
        for i in range(len(self.genre)):
            if self.genre[i] == equal:
                self.genre[i] = change

    def removeGenre(self, data):
        filter(lambda genre: genre == data, self.genre)

    def addBook(self, data):
        if(isinstance(data, str)):
            self.lob.append(data)
        else:
            print('Data not a string')

    def editBook(self, equal, change):
        for i in range(len(self.lob)):
            if self.lob[i] == equal:
                self.lob[i] = change

    def removeBook(self, data):
        filter(lambda book: book == data, self.lob)

    def editName(self, data):
        self.name = data

    def editDob(self, data):
        self.dob = data

    def editPwd(self, data):
        self.pwd = pbkdf2_sha256.hash(data)

    def editEmail(self, data):
        self.name = validate_email(data)

    def removeAuthor(self):
        return None


# ahmed = Author("mahmoud@gmail.com", "mahmoud")
# ahmed.addGenre("lo")
# ahmed.addGenre("boo")
# ahmed.addBook("boo")
# ahmed.addBook("kool")
# print(ahmed.genre)
# print(ahmed.lob)
