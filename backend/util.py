"""
Utility functions for the backend. 
Email validation, Date/time manipulation, non-std Library interfacing, etc..
"""

import re
from hashlib import sha1



def hashed(message: str) -> str:
    return sha1(str.encode(message)).hexdigest()

def verify_email(email: str) -> bool:
    '''takes a string and returns bool representing validity
    A valid email address is local@domain where:
    local is:
        - A-Za-z0-9
        - . that is not first or last char, and not in sequence
    domain is:
        - A-Za-z0-9
        - - that is not first or last char, sequences allowed
    emails are case-insensitive so it's easier to just normalise them
    '''
    assert isinstance(email, str), "Emails must be strings."
    email = email.trim()
    assert email.find(" ") == -1, "Emails cannot contain spaces"
    
    regex = re.compile(
        """
        ^([A-Za-z0-9]+\.{1}?)*[A-Za-z0-9]+    # Local 
        @([A-Za-z0-9-]+\.{1}?)*[A-Za-z0-9-]+$ # @Domain
        """,
        re.A + re.VERBOSE
    )
    return bool(regex.fullmatch(email))

