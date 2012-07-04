from sudeep_blog_post import SudeepBlogPostHandler
from sudeep_blog_display import SudeepBlogDisplayHandler
from sudeep_blog_permalink import SudeepBlogPermalinkHandler
from sudeep_blog_map import SudeepBlogMapHandler
from sudeep_blog_login import SudeepBlogLoginHandler
from sudeep_blog_logout import SudeepBlogLogoutHandler

import webapp2

app = webapp2.WSGIApplication([('/blog/newpost', SudeepBlogPostHandler), 
				('/blog', SudeepBlogDisplayHandler),
				('/blog/([0-9]+)', SudeepBlogPermalinkHandler),
				('/blog/map', SudeepBlogMapHandler),
				('/blog/login', SudeepBlogLoginHandler),
				('/blog/logout', SudeepBlogLogoutHandler)], 
				debug=True)
