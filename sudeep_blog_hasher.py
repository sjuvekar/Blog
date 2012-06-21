import hashlib
import random
import string

from sudeep_blog_user_db import SudeepBlogUserDB

__USER_ID_COOKIE__ = 'user_id'

def hash(username, password, salt=None):
        if not salt:
                salt = ""
                for i in range(0,10):
                        salt += random.choice(string.letters)
        return "{0}|{1}".format(hashlib.sha256(username + password + salt).hexdigest(), salt)

def validate(username, password, h):
	salt = h.split("|")[1]
	return h == hash(username, password, salt) 

def is_valid_cookie(cookie):
	tok = cookie.split("|")
	if len(tok) < 3:
		return False
	user_id = tok[0]
	password_hash = tok[1] + "|" + tok[2]
	retrieved_record = SudeepBlogUserDB.get_by_id(long(user_id))
	if retrieved_record and retrieved_record.sudeep_blog_db_password == password_hash:
		return True
	return False 
