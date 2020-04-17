'''Insert module docstring here'''

from util import _salt



class Author:
    '''Author class is resposnible for the Authors's data managment
    Atribs:
        name: str
        email: str
        dob (date of birth): tuple(Y, M, D)
        id: Int
        books: Set(Book)
    read-only:
        genres: Set(str)
    '''
    __AUTHOR_SALT = _salt("ath")
    _author_count = 0

    id = self.__inc()

    def __init__(self, name: str, dob: tuple, dod: tuple = (0,0,0)):
        self.name = name
        self.dob = dob
        self.dod = dod
        
        self._books = set()
        self._genres = set()

    @classmethod
    def __inc(cls): 
        cls._author_count += 1
        return cls._author_count

    @property
    def genres(self):
        if self._genres:
            return self._genres

        gset = set()
        for book in self.books:
            for g in book.genres:
                gset.add(g)
        return gset

    @property
    def books(self): return self._books

    @books.setter
    def books(self, bs): self._books = set(bs)

