#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Actor: logical group of classes that do most of the application activity

Classes:
    - Admin
    - User
"""

from .util import _hashed, _salt, _time, _seconds_of_days
from .book import Book as _Book



class _Actor:
    ''' The base class '''

    def __init__(self, email: str, passwd: str, name: str = "John Doe"):
        self.email = email
        self.passwd = _hashed(passwd)
        self.name = name

    @classmethod
    def _gen_id(cls, salt, count): return int(salt + str(count))

    @property
    def passwd(self): return self._passwd

    @passwd.setter
    def passwd(self, pstr): self._passwd = _hashed(pstr)



class Admin(_Actor):
    '''Admin class is responsible for all accountable db modifications
    and user management.

    Variables:
        - id     : int
        - email  : str
        - passwd : str, hashed
        - name   : str
    '''
    _SALT = _salt("adm")
    _count = 0

    def __init__(self, *args):
        super().__init__(*args)

        self._inc()
        self._id = super()._gen_id(self._SALT, self._count) 

    @classmethod
    def _inc(cls): cls._count += 1

    @property
    def id(self): return self._id

    def del_obj(self, obj_id: int):
        # Should check if obj is in runtime and delete it
        # Should check if obj is in DB and delete it
        pass


class User(Actor):
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
        pending: {Book : tuple(_time(), int(amount))}
        bought: {Book : tuple(_time(): int(amount))}
        borrowed: {Book : _time()}
        ratings: {Book : int(rating1-5)}
        reviews: {Book : str(comment)}
    '''

    _SALT = _salt("usr")
    _count = 0

    def __init__(self, name: str = "Anonymous", *args):
        super().__init__(*args)

        self._inc()
        self._id = super()._gen_id(self._SALT, self._count)

        self.name = name
        self.dob = None

        self._visa_serial = None
        self.address = ()

        self._borrowed = {}
        self._bought = {}
        self._pending = {}
        self._ratings = {}
        self._reviews = {}

    @property
    def id(self): return self._id

    @classmethod
    def _inc(cls): cls._count += 1

    @property
    def borrowed(self): return self._borrowed

    @property
    def pending(self): return self._pending

    @property
    def bought(self): return self._bought

    @property
    def ratings(self): return self._ratings

    @property
    def reviews(self): return self._reviews

    @property
    def visa_serial(self): return self._visa_serial

    @visa_serial.setter
    def visa_serial(self, serial: int) -> None:
        if len(str(serial)) < 12:
            raise ValueError('Invalid VISA serial number')
        else:
            self._visa_serial = serial

    def book_order(self, b: _book, num: int = 1) -> None:
        b.order(num)
        if self._pending[b.id]:
            self._pending[b.id] += _time(), num
        else:
            self._pending[b.id] = _time(), num

    def book_order_return(self, b: _Book, num: int = 1) -> None:
        #TODO: split this to two funcs, one for pending and one for bought
        if b.id in self._pending:
            if not num > pending_num:
                pending_num = self._pending[b.id][1]
                b.order_return(num)
            else:
                raise ValueError("Trying to return more than bought.")

        elif b.id in self._bought: # Split here probs
            warranty_s = _seconds_of_days(b.warranty)
            bought_since = self._bought[b.id][0]
            bought_num = self._bought[b.id][1]
            if warranty_s + bought_since > _time():
                if not num > bought_num:
                    b.order_return(num)
                else:
                raise ValueError("Trying to return more than bought.")
            else:    
                raise ValueError("Trying to return an expired book.")

        else: raise KeyError("trying to return a book you didn't buy.")

    def book_order_delivered(self, b: _Book, num: int = 1) -> None:
        pending_num = self._pending[b.id][1]
        if not b.id in self._pending:
            raise KeyError("Book is not pending.")

        if not num > pending_num:
            b.order_sold(num)
            if pending_num == num:
                del self._pending[b.id]
            else:
                self._pending[b.id][1] -= num
            if not self._bought[b.id]:
                self._bought[b.id] = _time(), num
            else:
                #TODO: for warranty management,
                # what if user ordered more of the same book?
                # 1. User shouldn't be treated like below
                # 2. Warranty shouldn't be renewed either
                # solution: keep track of every PURCHASE instead of every BOOK
                # this means Purchase and Borrow classes.
                # this will hopefully remove LOTS of complexity and redundancy
                # from both User and Book.
                self._bought[b.id][1] += num
        else:
            raise ValueError("Trying to flag more books than ordered.")

    # users can only borrow amount of one per book
    # the num parameter in Book.borrow is for future use.
    def book_borrow(self, b: _Book) -> None:
        if not self._borrowed][b.id]:
            b.borrow()
            self._borrowed[b.id] = time()
        else:
            raise KeyError("Trying to borrow an already-borrowed book.")

    def book_borrow_return(self, b: _Book) -> None:
        #TODO: use Book.borrow_limit for fining system
        if self._borrowed[b.id]:
            b.borrow_return()
            del self._borrowed[b.id]
        else:
            raise KeyError("Trying to return a book that wasn't borrowed.")

    def book_rate(self, b: _Book, rating: int) -> None:
        b.rate(self.id, rating)
        self._ratings[b.id] = rating

    def book_review(self, b: _Book, comment: str) -> None:
        b.review(self.id, comment)
        self.reviews[b.id] = comment

