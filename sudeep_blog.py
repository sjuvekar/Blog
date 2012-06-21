from sudeep_blog_post import SudeepBlogPostHandler
from sudeep_blog_display import SudeepBlogDisplayHandler
from sudeep_blog_permalink import SudeepBlogPermalinkHandler
from sudeep_blog_login import SudeepBlogLoginHandler

import webapp2

app = webapp2.WSGIApplication([('/blog/newpost', SudeepBlogPostHandler), 
				('/blog', SudeepBlogDisplayHandler),
				('/blog/([0-9]+)', SudeepBlogPermalinkHandler),
				('/blog/login', SudeepBlogLoginHandler)], 
				debug=True)
