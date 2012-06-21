from sudeep_blog_template import SudeepBlogTemplate
from sudeep_blog_user_db import SudeepBlogUserDB
import sudeep_blog_hasher 

from google.appengine.ext import db

__SUDEEP_BLOG_LOGIN_HTML__ = "sudeep_blog_login.html"

class SudeepBlogLoginHandler(SudeepBlogTemplate):
	def get(self):
		self.render(__SUDEEP_BLOG_LOGIN_HTML__, sudeep_blog_login_error = "")

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		user_query = db.GqlQuery("SELECT * FROM SudeepBlogUserDB WHERE sudeep_blog_db_username IN ('{0}')".format(username))
		hash_password_record = user_query.get()
		if hash_password_record and sudeep_blog_hasher.validate(username, password, hash_password_record.sudeep_blog_db_password):
			self.response.headers.add_header("Set-Cookie", "user_id={0}|{1}; Path=/".format(hash_password_record.key().id(), hash_password_record.sudeep_blog_db_password))
			self.redirect("/blog")
		else:
			self.render(__SUDEEP_BLOG_LOGIN_HTML__, sudeep_blog_login_error = "Incorrect Username and/or Password")
