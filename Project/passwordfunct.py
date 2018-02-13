#passwordfunct.py
import bcrypt


def make(password):
    """uses bcrypt library to produce a hash of the password """
    hashed = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
    return hashed


def check(rawpassword, passwordhash):
    """matches the hashed password in the database to the hash of the inputted password"""
    try:
        return bcrypt.checkpw(rawpassword.encode(),passwordhash)
    except TypeError:
        return False

