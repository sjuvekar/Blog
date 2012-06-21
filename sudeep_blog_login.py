from sudeep_blog_template import SudeepBlogTemplate
from sudeep_blog_user_db import SudeepBlogUserDB
import sudeep_blog_hasher 

__SUDEEP_BLOG_LOGIN_HTML__ = "sudeep_blog_login.html"

class SudeepBlogLoginHandler(SudeepBlogTemplate):
	def get(self):
		self.render(__SUDEEP_BLOG_LOGIN_HTML__, sudeep_blog_login_error = "")

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		if sudeep_blog_hasher.validate(username, password, "41b5194bbb126d47996c7d0678e1c526951801b3e75b416f4212449090c35f16|wolYapuTbK"):
			self.response.headers.add_header("Set-Cookie", "user_id=u")
			self.redirect("/blog")
		else:
			self.render(__SUDEEP_BLOG_LOGIN_HTML__, sudeep_blog_login_error = "Incorrect Username and/or Password")
