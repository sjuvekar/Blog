from google.appengine.ext import db

class SudeepBlogUserDB(db.Model):
        sudeep_blog_db_username = db.StringProperty(required = True)
        sudeep_blog_db_password = db.StringProperty(required = True)
        sudeep_blog_db_email = db.StringProperty()
        sudeep_blog_user_created = db.DateTimeProperty(auto_now_add = True)

