#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Actor: logical group of classes that do most of the application activity

Classes:
    - Admin
    - User
"""

from .util import _hashed



class Admin():
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

    def __init__(self, email: str, passwd: str, name= "Jon Doe"):
        self.email = email
        self.passwd = _hashed(passwd)
        self.name = name
        self.id = self.__inc()

    @classmethod
    def __inc(cls):
        cls._adm_count += 1
        return int(cls.__ADM_SALT + str(cls._adm_count))

    def get_info(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
            "passwd": "[REDACTED]"
        }
    
    def edit_info(self, inf: dict):
        self.__init__(
            inf.get("email") or self.email,
            inf.get("passwd") or self.passwd,
            inf.get("name") or self.name
        )

    def del_obj(self, obj_id: int):
        # Should check if obj is in runtime and delete it
        # Should check if obj is in DB and delete it
        pass

