#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Actor: logical group of classes that do most of the application activity

Classes:
    - Admin
    - User
"""

from .util import _hashed



class Admin:
    '''Admin class is responsible for all accountable db modifications 
    and user management.
    
    Variables:
        - email  : str
        - passwd : str, hashed
        - name   : str
    Methods:
        - 
    '''

    __ADM_SALT = "97100109"
    _adm_count = 0
    id = self.__inc()

    def __init__(self, email: str, passwd: str, name= "Jon Doe"):
        self.email = email
        self._passwd = _hashed(passwd)
        self.name = name

    @classmethod # classmethods are static
    def __inc(cls):
        cls._adm_count += 1
        return int(cls.__ADM_SALT + str(cls._adm_count))

    @property
    def passwd(self): return self._passwd
    
    @passwd.setter
    def passwd(self, passwd: str):
        self._passwd = _hashed(passwd)

    def del_obj(self, obj_id: int):
        # Should check if obj is in runtime and delete it
        # Should check if obj is in DB and delete it
        pass

