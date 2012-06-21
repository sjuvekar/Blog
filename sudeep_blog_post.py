from sudeep_blog_template import SudeepBlogTemplate
from sudeep_blog_db import SudeepBlogDB
import sudeep_blog_hasher

__SUDEEP_BLOG_POST_HTML__ = "sudeep_blog_post.html"

class SudeepBlogPostHandler(SudeepBlogTemplate):
  def render_blog(self, template, subject="", subject_error="", body="", body_error=""):
	self.render(template, sudeep_blog_subject=subject, sudeep_blog_subject_error=subject_error, sudeep_blog_body=body, sudeep_blog_body_error=body_error)

  def get(self):
	user_cookie = self.request.cookies.get("user_id")
	if user_cookie and sudeep_blog_hasher.is_valid_cookie(user_cookie): 	
		self.render_blog(__SUDEEP_BLOG_POST_HTML__)
	else:
		self.redirect("/blog/login") 	
	
  def post(self):
	subject = self.request.get("subject")
	body = self.request.get("content")
	# Checking if subject or body is empty
	if subject == "" or body == "":
		subject_error = ""
		body_error=""
		if subject == "":
			subject_error = "Subject can not be empty. Please create a suitable subject"
		if body == "":
			body_error = "Body can not be empty. Please add some text to your blog"
		self.render_blog(__SUDEEP_BLOG_POST_HTML__, subject, subject_error, body, body_error)
	else:
		db_entry = SudeepBlogDB(sudeep_blog_db_subject = subject, sudeep_blog_db_body = body)
		db_entry.put()
		self.redirect("/blog/{0}".format(db_entry.key().id()))

