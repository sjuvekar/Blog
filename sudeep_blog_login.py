from sudeep_blog_template import SudeepBlogTemplate

__SUDEEP_BLOG_LOGIN_HTML__ = "sudeep_blog_login.html"

class SudeepBlogLoginHandler(SudeepBlogTemplate):
	def get(self):
		self.render(__SUDEEP_BLOG_LOGIN_HTML__, sudeep_blog_login_error = "")

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		if username == "sjuvekar" and password == "speakfriendandenter":
			self.response.headers.add_header("Set-Cookie", "user_id=u")
			self.redirect("/blog")
		else:
			self.render(__SUDEEP_BLOG_LOGIN_HTML__, sudeep_blog_login_error = "Incorrect Username and/or Password")
