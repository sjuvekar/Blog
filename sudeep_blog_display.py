from sudeep_blog_template import SudeepBlogTemplate
from sudeep_blog_db import SudeepBlogDB
import sudeep_blog_hasher

from google.appengine.ext import db

__SUDEEP_BLOG_DISPLAY_HTML__ = "sudeep_blog_display.html"
__NUM_ENTRIES_PER_PAGE__ = 8

class SudeepBlogDisplayHandler(SudeepBlogTemplate):
	def head(self):
		pass
	
	def get(self):
		# Get the page and DB entries to display using page parameter
		page = self.request.get("page")
		if not page or not page.isdigit():
			page = 1
		page = int(page)
	 	num_entries_to_skip = (page - 1) * __NUM_ENTRIES_PER_PAGE__
		total_num_entries = SudeepBlogDB.all().count()
		if num_entries_to_skip >= total_num_entries:
			page = 1
			num_entries_to_skip = 0	
		blog_entries = SudeepBlogDB.all().order("-sudeep_blog_created").fetch(limit = __NUM_ENTRIES_PER_PAGE__, offset = num_entries_to_skip)
		
		# Get the custom links to previous and next pages
		pages_to_link = []
		for i in range(page-30, page+30):
			if i > 0 and (i - 1) * __NUM_ENTRIES_PER_PAGE__ < total_num_entries:
				pages_to_link.append(i)
		
		# Finally create a login/logout link 	
		sudeep_blog_login = "login"
		user_cookie = self.request.cookies.get("user_id")
		if user_cookie and sudeep_blog_hasher.is_valid_cookie(user_cookie):
			sudeep_blog_login = "logout"
		
		self.render(__SUDEEP_BLOG_DISPLAY_HTML__, blog_entries = blog_entries, sudeep_blog_login = sudeep_blog_login, pages_to_link = pages_to_link)
