from sudeep_blog_template import SudeepBlogTemplate
from sudeep_blog_db import SudeepBlogDB

from google.appengine.ext import db

__SUDEEP_BLOG_DISPLAY_HTML__ = "sudeep_blog_display.html"

class SudeepBlogDisplayHandler(SudeepBlogTemplate):
	def get(self):
		blog_entries = db.GqlQuery("SELECT * FROM SudeepBlogDB ORDER BY sudeep_blog_created DESC")
		self.render(__SUDEEP_BLOG_DISPLAY_HTML__, blog_entries = blog_entries)
