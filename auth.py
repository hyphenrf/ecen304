from hashlib import sha1
import re

def _auth(session, admins):
    token = session['id']
    def auth_inner(fn):
        def wrap(*args, **kwargs):
            if token in admins:
                return fn(*args, **kwargs)
            else:
                return {"status": "error: forbidden"}
        return wrap
    return auth_inner

def hashed(message: str):
    return sha1(str.encode(message)).hexdigest()

def verify_email(email: str):
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
    email = email.strip()
    assert email.find(" ") == -1, "Emails cannot contain spaces"

    regex = re.compile(
        """
        ^([A-Za-z0-9]+\.{1}?)*[A-Za-z0-9]+    # Local 
        @([A-Za-z0-9-]+\.{1}?)*[A-Za-z0-9-]+$ # @Domain
        """,
        re.A + re.VERBOSE
    )
    return bool(regex.fullmatch(email))
