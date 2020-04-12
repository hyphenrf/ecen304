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

    def __init__(self, email, passwd, name= "Jon Doe"):
        
        assert verify_email(email) == True, "Invalid Email property"

        self.email = email.trim()
        self.passwd = hashed(passwd)
        self.name = name
