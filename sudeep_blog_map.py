from sudeep_blog_template import SudeepBlogTemplate
from sudeep_blog_db import SudeepBlogDB

from google.appengine.ext import db

__SUDEEP_BLOG_MAP_HTM__ = "sudeep_blog_map.html"

class SudeepBlogMapHandler(SudeepBlogTemplate):
	def get(self):
		blog_entries = SudeepBlogDB.all()
		static_map_url = "http://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&size=900x450&sensor=false"
		for entry in blog_entries:
			if entry.sudeep_blog_coords:
				static_map_url += "&markers={0},{1}".format(entry.sudeep_blog_coords.lat, entry.sudeep_blog_coords.lon)
		self.render(__SUDEEP_BLOG_MAP_HTM__, static_map_url = static_map_url)
