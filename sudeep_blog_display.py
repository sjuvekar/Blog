from sudeep_blog_template import SudeepBlogTemplate
from sudeep_blog_db import SudeepBlogDB
import sudeep_blog_hasher

from google.appengine.ext import db

__SUDEEP_BLOG_DISPLAY_HTML__ = "sudeep_blog_display.html"

class SudeepBlogDisplayHandler(SudeepBlogTemplate):
	def head(self):
		pass
	
	def get(self):
		blog_entries = db.GqlQuery("SELECT * FROM SudeepBlogDB ORDER BY sudeep_blog_created DESC")
		sudeep_blog_login = "login"
		user_cookie = self.request.cookies.get("user_id")
		if user_cookie and sudeep_blog_hasher.is_valid_cookie(user_cookie):
			sudeep_blog_login = "logout"
		self.render(__SUDEEP_BLOG_DISPLAY_HTML__, blog_entries = blog_entries, sudeep_blog_login = sudeep_blog_login)
