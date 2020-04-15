from .util import _hashed


class Author:
    '''Author class is resposnible for the Authors's data modification and managment
    Atribs:
        ID: Int
        Name: String
        Date of birth (dob): Int:EPOCH
        List of books (lob): List<Int:ID>
        Genres: List<String>
        Email: str
        Password (pwd): str

    Methods:
        # ADDING => adding the author is done when the class instance is initiated
        addGenre()
        addBook()

        # EDITING
        editGenre()
        editBook()
        editName()
        editDob()
        editPwd()
        editEmail()

        # REMOVING
        removeGenre()
        removeBook()
        removeAuthor()
    '''

    def __init__(self, email: str, pwd: str, name='Jay', dob=None):

        # ASSERTIONS
        assert isinstance(pwd, str), "Password must be a string"
        assert isinstance(email, str), "Email must be a string"
        assert isinstance(name, str), "Name must be a string"

        self.name = name
        self.dob = dob
        self.email = email
        self.pwd = _hashed(pwd)
        self.genre = []
        self.lob = []

    def add_genre(self, Genre: str) -> list:
        if(isinstance(Genre, str)):
            self.genre.append(Genre)
        else:
            print('Data not a string')
        return self.genre

    def edit_genre(self, old: str, new: str) -> list:
        for i in range(len(self.genre)):
            if self.genre[i] == old:
                self.genre[i] = new
        return self.genre

    def remove_genre(self, data: str) -> list:
        filter(lambda genre: genre == str, self.genre)
        return self.genre

    def add_book(self, book: str) -> list:
        if(isinstance(book, str)):
            self.lob.append(book)
        else:
            print('Data not a string')
        return self.lob

    def edit_book(self, old: str, new: str) -> list:
        for i in range(len(self.lob)):
            if self.lob[i] == old:
                self.lob[i] = new
        return self.lob

    def remove_book(self, data: str) -> list:
        filter(lambda book: book == data, self.lob)
        return self.lob

    def edit_name(self, name: str) -> str:
        self.name = name
        return self.name

    def edit_dob(self, data):
        self.dob = data
        return self.dob

    def edit_pwd(self, data):
        self.pwd = _hashed(data)

    def edit_email(self, data):
        self.name = data
        return self.email

    def remove_author(self, id):
        return None
