from sudeep_blog_template import SudeepBlogTemplate
from sudeep_blog_db import SudeepBlogDB
import sudeep_blog_hasher

from google.appengine.ext import db

__SUDEEP_BLOG_DISPLAY_HTML__ = "sudeep_blog_display.html"
__NUM_ENTRIES_PER_PAGE__ = 10

class SudeepBlogDisplayHandler(SudeepBlogTemplate):
	def head(self):
		pass
	
	def get(self):
		page = self.request.get("page")
		if not page or not page.isdigit():
			page = 1
		page = int(page)
	 	num_entries_to_skip = (page - 1) * __NUM_ENTRIES_PER_PAGE__
		if num_entries_to_skip >= SudeepBlogDB.all().count():
			page = 1
			num_entries_to_skip = 0	
		blog_entries = SudeepBlogDB.all().order("-sudeep_blog_created").fetch(limit = __NUM_ENTRIES_PER_PAGE__, offset = num_entries_to_skip)
		sudeep_blog_login = "login"
		user_cookie = self.request.cookies.get("user_id")
		if user_cookie and sudeep_blog_hasher.is_valid_cookie(user_cookie):
			sudeep_blog_login = "logout"
		self.render(__SUDEEP_BLOG_DISPLAY_HTML__, blog_entries = blog_entries, sudeep_blog_login = sudeep_blog_login)
