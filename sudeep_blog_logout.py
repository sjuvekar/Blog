from sudeep_blog_template import SudeepBlogTemplate

class SudeepBlogLogoutHandler(SudeepBlogTemplate):
	def get(self):
		self.response.headers.add_header("Set-Cookie", "user_id=; Path=/")
		self.redirect("/blog")
