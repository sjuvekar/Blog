from sudeep_blog_template import SudeepBlogTemplate

class SudeepBlogLoginHandler(SudeepBlogTemplate):
	def get(self):
		self.render("sudeep_blog_login.html")
