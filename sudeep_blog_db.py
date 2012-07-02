from google.appengine.ext import db

class SudeepBlogDB(db.Model):
	sudeep_blog_db_subject = db.TextProperty(required = True)
	sudeep_blog_db_body = db.TextProperty(required = True)
	sudeep_blog_created = db.DateTimeProperty(auto_now_add = True)
	sudeep_blog_coords = db.GeoPtProperty()
