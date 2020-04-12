#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Actor: logical group of classes that do most of the application activity

Classes:
    - Admin
    - User
"""

from util import verify_email, hashed



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
        
        # assertion checks. Will remove on external interfacing
        assert verify_email(email) == True, "Invalid Email property"
        assert isinstance(passwd, str), "Password must be a string"
        assert isinstance(name, str), "Name must be a string"

        self.email = email.trim()
        self.passwd = hashed(passwd)
        self.name = name
        self.id = self.__inc()

    @classmethod
    def __inc(self):
        self._adm_count += 1
        return int(__ADM_SALT + str(self._adm_count))

    def del_obj(obj_id: int):
        # Should check if obj is in runtime and delete it
        # Should check if obj is in DB and delete it
        pass



