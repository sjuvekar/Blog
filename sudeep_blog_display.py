from sudeep_blog_template import SudeepBlogTemplate
from sudeep_blog_db import SudeepBlogDB

from google.appengine.ext import db

__SUDEEP_BLOG_DISPLAY_HTML__ = "sudeep_blog_display.html"

class SudeepBlogDisplayHandler(SudeepBlogTemplate):
	def get(self):
		blog_entries = db.GqlQuery("SELECT * FROM SudeepBlogDB ORDER BY sudeep_blog_created DESC")
		sudeep_blog_login = "login"
		user_id = self.request.cookies.get("user_id")
		if user_id:
			sudeep_blog_login = "logout"
		self.render(__SUDEEP_BLOG_DISPLAY_HTML__, blog_entries = blog_entries, sudeep_blog_login = sudeep_blog_login)
