from sudeep_blog_post import SudeepBlogPostHandler
from sudeep_blog_display import SudeepBlogDisplayHandler
from sudeep_blog_permalink import SudeepBlogPermalinkHandler

import webapp2

app = webapp2.WSGIApplication([('/blog/newpost', SudeepBlogPostHandler), 
				('/blog', SudeepBlogDisplayHandler),
				('/blog/([0-9]+)', SudeepBlogPermalinkHandler)], 
				debug=True)
