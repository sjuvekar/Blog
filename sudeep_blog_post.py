from sudeep_blog_template import SudeepBlogTemplate
from sudeep_blog_db import SudeepBlogDB
from google.appengine.ext import db
import sudeep_blog_hasher
import urllib2
from xml.dom import minidom

__SUDEEP_BLOG_POST_HTML__ = "sudeep_blog_post.html"
__HTTP_INFO_STRING__ = "http://api.hostip.info/?ip="

class SudeepBlogPostHandler(SudeepBlogTemplate):
  def render_blog(self, template, subject="", subject_error="", body="", body_error=""):
	self.render(template, sudeep_blog_subject=subject, sudeep_blog_subject_error=subject_error, sudeep_blog_body=body, sudeep_blog_body_error=body_error)

  def _get_coords(self, location_ip):
	if not location_ip:
		return None
 	ip_xml_string = __HTTP_INFO_STRING__ + location_ip
	xml = urllib2.urlopen(ip_xml_string).read()
	if not xml:
		return None
	xml_object = minidom.parseString(xml)
	coords_tag = xml_object.getElementsByTagName("gml:coordinates")
	if coords_tag and len(coords_tag) > 0 and coords_tag[0].childNodes and len(coords_tag[0].childNodes) > 0:
		longitude, lattitude = coords_tag[0].childNodes[0].nodeValue.split(",")
		return lattitude, longitude	

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
		location_ip = self.request.remote_addr
		coords = self._get_coords(location_ip)
		if coords:
			db_entry = SudeepBlogDB(sudeep_blog_db_subject = subject, sudeep_blog_db_body = body, sudeep_blog_coords = db.GeoPt(coords[0], coords[1]))
		else:	
			db_entry = SudeepBlogDB(sudeep_blog_db_subject = subject, sudeep_blog_db_body = body)
		db_entry.put()
		self.redirect("/blog/{0}".format(db_entry.key().id()))

