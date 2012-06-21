from sudeep_blog_template import SudeepBlogTemplate
from sudeep_blog_db import SudeepBlogDB

from google.appengine.ext import db

__SUDEEP_BLOG_PERMALINK_HTML__ = "sudeep_blog_permalink.html"


class SudeepBlogPermalinkHandler(SudeepBlogTemplate):
  def get(self, sudeep_blog_id):
        blog_entry = SudeepBlogDB.get_by_id(long(sudeep_blog_id))
	if not blog_entry:
                self.error(404)
                return
        else:
                self.render(__SUDEEP_BLOG_PERMALINK_HTML__, blog_entry = blog_entry)

